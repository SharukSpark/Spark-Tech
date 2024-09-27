
from django.shortcuts import render,redirect
from sparktechapp.models import processor,motherboard,graphiccard,coolingsystem,ram,smbs,ssd,harddrive,CART,OrderItem,Order
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.conf import settings
import razorpay




def home(request):
    if request.user.is_authenticated:
        userid = request.user.id
        cart_items = CART.objects.filter(uid=userid)

        # Calculate the total number of items in the cart
        n = sum(item.qty for item in cart_items)

        context = {
            'n': n,
        }
    else:
        # Provide default values when the user is not authenticated
        context = {
            'n': 0,  # Default value when not logged in
        }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def viewcart(request):
    if request.user.is_authenticated:
        userid = request.user.id
        cart_items = CART.objects.filter(uid=userid)
        
        subtotal1 = 0
        subtotal2 = 0
        subtotal3 = 0
        subtotal4 = 0
        subtotal5 = 0
        subtotal6 = 0
        subtotal7 = 0
        

        Processor = []
        Motherboard=[]
        Graphiccard=[]
        Coolingsystem=[]
        Ram=[]
        Ssd=[]
        Smbs=[]

        
        for item in cart_items:
            if item.Processor:
                subtotal1 = item.Processor.price * item.qty
                Processor.append({
                    'item': item,
                    'subtotal1': subtotal1
                })
            elif item.Motherboard:
                subtotal2 = item.Motherboard.price * item.qty
                Motherboard.append({
                    'item': item,
                    'subtotal2': subtotal2
                })
            elif item.Graphiccard:
                subtotal3 = item.Graphiccard.price * item.qty
                Graphiccard.append({
                    'item': item,
                    'subtotal3': subtotal3
                })
            elif item.Coolingsystem:
                subtotal4 = item.Coolingsystem.price * item.qty
                Coolingsystem.append({
                    'item': item,
                    'subtotal4': subtotal4
                })
            elif item.Ram:
                subtotal5 = item.Ram.price * item.qty
                Ram.append({
                    'item': item,
                    'subtotal5': subtotal5
                })
            elif item.Ssd:
                subtotal6 = item.Ssd.price * item.qty
                Ssd.append({
                    'item': item,
                    'subtotal6': subtotal6
                })
            elif item.Smbs:
                subtotal7 = item.Smbs.price * item.qty
                Smbs.append({
                    'item': item,
                    'subtotal7': subtotal7
                })
        
        maintotal = subtotal1+subtotal2+subtotal3+subtotal4+subtotal5+subtotal6+subtotal7
        # shipping_cost = 1000  # Assuming $10 shipping for simplicity
        # total = maintotal + shipping_cost
        total = maintotal
        n = sum(item.qty for item in cart_items)

        context = {
            'Processor': Processor,
            'subtotal1':subtotal1,

            'Motherboard': Motherboard,
            'subtotal2':subtotal2,

            'Graphiccard': Graphiccard,
            'subtotal3':subtotal3,

            'Coolingsystem': Coolingsystem,
            'subtotal4':subtotal4,

            'Ram': Ram,
            'subtotal5':subtotal5,

            'Ssd': Ssd,
            'subtotal6':subtotal6,

            'Smbs': Smbs,
            'subtotal7':subtotal7,

            'maintotal': maintotal,
            'total': total,
            'n': n,
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('/login')
    
def remove(request, cid):
    c = CART.objects.filter(id=cid)
    c.delete()
    return redirect('/cart')

def updateqty(request, qv, cid):
    c = CART.objects.filter(id=cid)
    if c.exists():
        if qv == '1':
            t = c[0].qty + 1
            c.update(qty=t)
        elif qv == '0':
            if c[0].qty > 1:
                t = c[0].qty - 1
                c.update(qty=t)
    return redirect('/cart')  # Redirect to the cart page

def calculate_shipping_cost(order):
    # Example calculation: flat rate or based on order total
    if order.total > 10000:
        return 0  # Free shipping for orders over 1000
    else:
        return 1000  # Flat rate shipping

def account_view(request):
    # Fetch the latest order for the logged-in user
    latest_order = Order.objects.filter(user=request.user).order_by('-created_at').first()

    context = {
        'latest_order': latest_order,
    }

    return render(request, 'account.html', context)

def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = []
    subtotal = 0
    
    for item in order.items.all():
        item_total = item.quantity * item.price
        subtotal += item_total
        order_items.append({'product': item.product, 'quantity': item.quantity, 'price': item.price, 'total': item_total})
    
    
    shipping_cost = calculate_shipping_cost(order)
    grand_total = subtotal + shipping_cost
    
    context = {
        'order': order,
        'order_items': order_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,  # Add shipping cost to the context
        'grand_total': grand_total,      # Add grand total to the context
    }
    
    return render(request, 'invoice.html', context)

def checkout(request):
    if request.user.is_authenticated:
        userid = request.user.id
        cart_items = CART.objects.filter(uid=userid)

        # Calculate subtotals for each item type
        subtotal1 = sum(item.qty * item.Processor.price for item in cart_items if item.Processor)
        subtotal2 = sum(item.qty * item.Motherboard.price for item in cart_items if item.Motherboard)
        subtotal3 = sum(item.qty * item.Graphiccard.price for item in cart_items if item.Graphiccard)
        subtotal4 = sum(item.qty * item.Coolingsystem.price for item in cart_items if item.Coolingsystem)
        subtotal5 = sum(item.qty * item.Ram.price for item in cart_items if item.Ram)
        subtotal6 = sum(item.qty * item.Ssd.price for item in cart_items if item.Ssd)
        subtotal7 = sum(item.qty * item.Smbs.price for item in cart_items if item.Smbs)

        maintotal = subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5 + subtotal6 + subtotal7
        total = maintotal 
        n = sum(item.qty for item in cart_items)

        context = {
            'maintotal': maintotal,
            'total': total,
            'n': n,
        }

        if request.method == 'POST':
            first_name = request.POST['first_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address1 = request.POST['address1']
            city = request.POST['city']
            state = request.POST['state']
            zipcode = request.POST['zipcode']

            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                email=email,
                phone=phone,
                address1=address1,
                city=city,
                state=state,
                zipcode=zipcode,
                total=total
            )

            # Create OrderItem objects
            for item in cart_items:
                if item.Processor:
                    product_name = item.Processor.name
                    price = item.Processor.price
                elif item.Motherboard:
                    product_name = item.Motherboard.name
                    price = item.Motherboard.price
                elif item.Graphiccard:
                    product_name = item.Graphiccard.name
                    price = item.Graphiccard.price
                elif item.Coolingsystem:
                    product_name = item.Coolingsystem.name
                    price = item.Coolingsystem.price
                elif item.Ram:
                    product_name = item.Ram.name
                    price = item.Ram.price
                elif item.Ssd:
                    product_name = item.Ssd.name
                    price = item.Ssd.price
                elif item.Smbs:
                    product_name = item.Smbs.name
                    price = item.Smbs.price

                OrderItem.objects.create(
                    order=order,
                    product=product_name,
                    quantity=item.qty,
                    price=price
                )

            # Clear the cart after the order is placed
            # cart_items.delete()

            return redirect('shipping', order_id=order.id)
        else:
            last_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
            initial_data = {
                'first_name': last_order.first_name if last_order else '',
                'email': last_order.email if last_order else '',
                'phone': last_order.phone if last_order else '',
                'address1': last_order.address1 if last_order else '',
                'city': last_order.city if last_order else '',
                'state': last_order.state if last_order else '',
                'zipcode': last_order.zipcode if last_order else '',
            }

            context.update({'initial_data': initial_data})
            return render(request, 'checkout.html', context)
    else:
        return redirect('login')

def shipping(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = []
    subtotal = 0
    
    for item in order.items.all():
        item_total = item.quantity * item.price
        subtotal += item_total
        order_items.append({'product': item.product, 'quantity': item.quantity, 'price': item.price, 'total': item_total})
    
    
    shipping_cost = calculate_shipping_cost(order)
    grand_total = subtotal + shipping_cost
    
    context = {
        'order': order,
        'order_items': order_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,  # Add shipping cost to the context
        'grand_total': grand_total,      # Add grand total to the context
    }
    
    return render(request, 'shipping.html', context)

# Initialize Razorpay client with provided credentials
razorpay_client = razorpay.Client(auth=("rzp_test_VZbpcH0s33sGpv", "nKMohKrV5iNczM3REH4R1YeR"))

def payment(request, id):
    # Retrieve the specific order using the provided id
    order = get_object_or_404(Order, id=id)
    
    # Calculate the shipping cost
    shipping_cost = calculate_shipping_cost(order)
    
    # Add the shipping cost to the grand total
    grand_total = order.total + shipping_cost
    
    # Convert the total into paisa (for Razorpay)
    amount_in_paisa = int(grand_total * 100)
    
    # Pass the amount in paisa and shipping cost to the template for display or processing
    context = {
        'order': order,
        'amount_in_paisa': amount_in_paisa,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,  # If you want to display the grand total with shipping in the template
    }
    return render(request, 'pay.html', context)

################################ cart start ################################################################

def cart(request):

    return render(request, 'cart.html')

def addtocart_1(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=userid, Smbs_id=pid).exists():
                u = User.objects.get(id=userid)
                p = smbs.objects.get(id=pid)
                
                # Add the product to the cart
                c = CART.objects.create(uid=u, Smbs=p)
                c.save()
                
                # Prepare context to render in home.html
               
                return redirect('/cart')
            
            else:
                # The product is already in the cart
                messages.info(request, 'This product is already in your cart. You can only increase the quantity.')
                return redirect('/cart')
        
        except ValueError:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
        
    else:
        return redirect('/login')
       
def addtocart_2(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=userid, Processor_id=pid).exists():
                u = User.objects.get(id=userid)
                p = processor.objects.get(id=pid)
                
                # Add the product to the cart
                c = CART.objects.create(uid=u, Processor=p)
                c.save()
                
                # Redirect to the cart page after adding the product
                return redirect('/cart')
            
            else:
                # The product is already in the cart, handle it accordingly
                messages.info(request, 'This product is already in your cart.So you can increase the quantity only')
                return redirect('/cart')
        
        except ValueError:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
       
    else:
        return redirect('/login')

def addtocart_3(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            u = User.objects.get(id=userid)
            p = motherboard.objects.get(id=pid)

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=u, Motherboard=p).exists():
                # Add the product to the cart
                c = CART.objects.create(uid=u, Motherboard=p)
                c.save()

                # Redirect to the cart page after adding the product
                return redirect('/cart')
            else:
                # The product is already in the cart
                messages.info(request, 'This product is already in your cart. You can increase the quantity only.')
                return redirect('/cart')
        
        except motherboard.DoesNotExist:
            # Handle the case where the motherboard does not exist
            messages.error(request, 'The product you are trying to add does not exist.')
            return redirect('/cart')
        
        except ValueError:
            # Handle other potential errors
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
        
    else:
        return redirect('/login')

def addtocart_4(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            u = User.objects.get(id=userid)
            p = graphiccard.objects.get(id=pid)

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=u, Graphiccard=p).exists():
                # Add the product to the cart
                c = CART.objects.create(uid=u, Graphiccard=p)
                c.save()

                # Redirect to the cart page after adding the product
                return redirect('/cart')
            else:
                # The product is already in the cart
                messages.info(request, 'This product is already in your cart. You can increase the quantity only.')
                return redirect('/cart')
        
        except graphiccard.DoesNotExist:
            # Handle the case where the graphiccard does not exist
            messages.error(request, 'The product you are trying to add does not exist.')
            return redirect('/cart')
        
        except ValueError:
            # Handle other potential errors
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
        
    else:
        return redirect('/login')

def addtocart_5(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            u = User.objects.get(id=userid)
            p = coolingsystem.objects.get(id=pid)

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=u, Coolingsystem=p).exists():
                # Add the product to the cart
                c = CART.objects.create(uid=u, Coolingsystem=p)
                c.save()

                # Redirect to the cart page after adding the product
                return redirect('/cart')
            else:
                # The product is already in the cart
                messages.info(request, 'This product is already in your cart. You can increase the quantity only.')
                return redirect('/cart')
        
        except coolingsystem.DoesNotExist:
            # Handle the case where the coolingsystem does not exist
            messages.error(request, 'The product you are trying to add does not exist.')
            return redirect('/cart')
        
        except ValueError:
            # Handle other potential errors
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
        
    else:
        return redirect('/login')

def addtocart_6(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            u = User.objects.get(id=userid)
            p = ram.objects.get(id=pid)

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=u, Ram=p).exists():
                # Add the product to the cart
                c = CART.objects.create(uid=u, Ram=p)
                c.save()

                # Redirect to the cart page after adding the product
                return redirect('/cart')
            else:
                # The product is already in the cart
                messages.info(request, 'This product is already in your cart. You can increase the quantity only.')
                return redirect('/cart')
        
        except ram.DoesNotExist:
            # Handle the case where the ram does not exist
            messages.error(request, 'The product you are trying to add does not exist.')
            return redirect('/cart')
        
        except ValueError:
            # Handle other potential errors
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
        
    else:
        return redirect('/login')

def addtocart_7(request, pid):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            u = User.objects.get(id=userid)
            p = ssd.objects.get(id=pid)

            # Check if the product is already in the user's cart
            if not CART.objects.filter(uid=u, Ssd=p).exists():
                # Add the product to the cart
                c = CART.objects.create(uid=u, Ssd=p)
                c.save()

                # Redirect to the cart page after adding the product
                return redirect('/cart')
            else:
                # The product is already in the cart
                messages.info(request, 'This product is already in your cart. You can increase the quantity only.')
                return redirect('/cart')
        
        except ssd.DoesNotExist:
            # Handle the case where the ssd does not exist
            messages.error(request, 'The product you are trying to add does not exist.')
            return redirect('/cart')
        
        except ValueError:
            # Handle other potential errors
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/cart')
        
    else:
        return redirect('/login')

################################ cart end ##################################################################

################################ motherboard start #########################################################

def motherboarddetails(request, pid):
    context = {}
    context['motherboard'] = motherboard.objects.filter(id=pid, is_active=True)
    return render(request, 'motherboarddetails.html', context)

def motherboardlist(request):
    return render(request, 'motherboard.html')

def DDR_5(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['motherboard'] = motherboard.objects.filter(q1 & q2)
    return render(request, 'DDR_5.html', context)

def ThreadRipper(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['motherboard'] = motherboard.objects.filter(q1 & q2)
    return render(request, 'ThreadRipper.html', context)

def board_650(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['motherboard'] = motherboard.objects.filter(q1 & q2)
    return render(request, 'board_650.html', context)

def board_550(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['motherboard'] = motherboard.objects.filter(q1 & q2)
    return render(request, 'board_550.html', context)

def board_450(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=5)
    context['motherboard'] = motherboard.objects.filter(q1 & q2)
    return render(request, 'board_450.html', context)


################################ motherboard end ############################################################


############################### graphic card start ##########################################################

def graphiccargdetails(request, pid):
    context = {}
    context['graphiccard'] = graphiccard.objects.filter(id=pid, is_active=True)
    return render(request, 'graphiccargdetails.html', context)

def graphiccardlist(request):
    return render(request, 'graphiccard.html')

def Cards_4060(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['graphiccard'] = graphiccard.objects.filter(q1 & q2)
    return render(request, 'Cards_4060.html', context)

def Cards_3050(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['graphiccard'] = graphiccard.objects.filter(q1 & q2)
    return render(request, 'Cards_3050.html', context)

def Cards_1650(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['graphiccard'] = graphiccard.objects.filter(q1 & q2)
    return render(request, 'Cards_1650.html', context)


################################ graphic card end ###########################################################


############################## cooling system start #########################################################

def coolingsystemdetails(request, pid):
    context = {}
    context['coolingsystem'] = coolingsystem.objects.filter(id=pid, is_active=True)
    return render(request, 'coolingsystemdetails.html', context)

def coolingsystemdlist(request):
    return render(request, 'coolingsystem.html')

def Cooler_360mm(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['coolingsystem'] = coolingsystem.objects.filter(q1 & q2)
    return render(request, 'Cooler360mm.html', context)

def Cooler_240mm(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['coolingsystem'] = coolingsystem.objects.filter(q1 & q2)
    return render(request, 'Cooler_240mm.html', context)

def Cooler_120mm(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['coolingsystem'] = coolingsystem.objects.filter(q1 & q2)
    return render(request, 'Cooler_120mm.html', context)

def Custom_RGB_Cooler(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['coolingsystem'] = coolingsystem.objects.filter(q1 & q2)
    return render(request, 'Custom_RGB_Cooler.html', context)

def CPU_RGB_Cooler(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=5)
    context['coolingsystem'] = coolingsystem.objects.filter(q1 & q2)
    return render(request, 'CPU_RGB_Cooler.html', context)

################################ cooling system end #########################################################


################################# processor start ###########################################################

def processordetails(request, pid):
    context = {}
    context['processor'] = processor.objects.filter(id=pid, is_active=True)
    return render(request, 'processordetails.html', context)

def processorlist(request):
    return render(request, 'processor.html')

def ryzen3(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'ryzen3.html', context)

def ryzen5(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'ryzen5.html', context)

def ryzen7(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'ryzen7.html', context)

def ryzen9(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'ryzen9.html', context)

def Threadripper_Series(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=5)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'Threadripper_Series.html', context)

def i3_Series(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=6)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'i3_Series.html', context)

def i5_Series(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=7)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'i5_Series.html', context)

def i7_Series(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=8)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'i7_Series.html', context)

def i9_Series(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=9)
    context['processor'] = processor.objects.filter(q1 & q2)
    return render(request, 'i9_Series.html', context)

################################ processor end ##############################################################

################################## ram start ################################################################

def ramdetails(request, pid):
    context = {}
    context['ram'] = ram.objects.filter(id=pid, is_active=True)
    return render(request, 'ramdetails.html', context)

def ramlist(request):
    return render(request, 'ram.html')

def Ram_8GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['ram'] = ram.objects.filter(q1 & q2)
    return render(request, 'Ram_8GB.html', context)

def Ram_16GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['ram'] = ram.objects.filter(q1 & q2)
    return render(request, 'Ram_16GB.html', context)

def Ram_32GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['ram'] = ram.objects.filter(q1 & q2)
    return render(request, 'Ram_32GB.html', context)

def Ram_64GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['ram'] = ram.objects.filter(q1 & q2)
    return render(request, 'Ram_64GB.html', context)


################################# ram end ###################################################################

################################ ssd start ##################################################################

def ssddetails(request, pid):
    context = {}
    context['ssd'] = ssd.objects.filter(id=pid, is_active=True)
    return render(request, 'ssddetails.html', context)

def ssdlist(request):
    return render(request, 'ssd.html')

def ssd_256GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['ssd'] = ssd.objects.filter(q1 & q2)
    return render(request, 'ssd_256GB.html', context)

def ssd_500GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['ssd'] = ssd.objects.filter(q1 & q2)
    return render(request, 'ssd_500GB.html', context)

def M_2_NVMe_256GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['ssd'] = ssd.objects.filter(q1 & q2)
    return render(request, 'M_2_NVMe_256GB.html', context)

def M_2_NVMe_500GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['ssd'] = ssd.objects.filter(q1 & q2)
    return render(request, 'M_2_NVMe_500GB.html', context)

def M_2_NVMe_1TB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=5)
    context['ssd'] = ssd.objects.filter(q1 & q2)
    return render(request, 'M_2_NVMe_1TB.html', context)

################################### ssd end #################################################################

################################ harddisk start #############################################################
def harddrivedetails(request, pid):
    context = {}
    context['harddrive'] = harddrive.objects.filter(id=pid, is_active=True)
    return render(request, 'harddrivedetails.html', context)

def hddlist(request):
    return render(request, 'hdd.html')

def hdd_256GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['harddrive'] = harddrive.objects.filter(q1 & q2)
    return render(request, 'hdd_256GB.html', context)

def hdd_500GB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['harddrive'] = harddrive.objects.filter(q1 & q2)
    return render(request, 'hdd_500GB.html', context)

def hdd_1TB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['harddrive'] = harddrive.objects.filter(q1 & q2)
    return render(request, 'hdd_1TB.html', context)

def hdd_2TB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['harddrive'] = harddrive.objects.filter(q1 & q2)
    return render(request, 'hdd_2TB.html', context)

def hdd_4TB(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=5)
    context['harddrive'] = harddrive.objects.filter(q1 & q2)
    return render(request, 'hdd_4TB.html', context)
################################ harddisk end ###############################################################

################################ smbs start #################################################################

def smbsdetails(request, pid):
    context = {}
    context['smbs'] = smbs.objects.filter(id=pid, is_active=True)
    return render(request, 'smbsdetails.html', context)

def smbslist(request):
    return render(request, 'smbs.html')

def smbs_400W(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=1)
    context['smbs'] = smbs.objects.filter(q1 & q2)
    return render(request, 'smbs_400W.html', context)

def smbs_500W(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=2)
    context['smbs'] = smbs.objects.filter(q1 & q2)
    return render(request, 'smbs_500W.html', context)

def smbs_600W(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=3)
    context['smbs'] = smbs.objects.filter(q1 & q2)
    return render(request, 'smbs_600W.html', context)

def smbs_800W(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=4)
    context['smbs'] = smbs.objects.filter(q1 & q2)
    return render(request, 'smbs_800W.html', context)

def smbs_1000W(request):
    context = {}
    q1 = Q(is_active=True)
    q2 = Q(cat=5)
    context['smbs'] = smbs.objects.filter(q1 & q2)
    return render(request, 'smbs_1000W.html', context)

################################# smbs end ##################################################################

################################# login start ###############################################################

def logoutdetails(request):
    logout(request)
    return redirect ('/home')

def logindetails(request):
    context = {}  # Initialize context as an empty dictionary
    if request.method == "POST":
        loginName = request.POST['uname']
        loginPassword = request.POST['upass']
        if loginName == '' or loginPassword == '':
            context["errormessage"] = "Field cannot be blank"  # Fixed typo from "blanck" to "blank"
            return render(request, 'login.html', context)
        else:
            u = authenticate(username=loginName, password=loginPassword)
            print(u)
            if u is not None:
                login(request, u)
                return redirect('/home')
            else:
                context['errormessage'] = "Invalid user"
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def registerdetails(request):
    if request.method=="POST":
         context={}
         userName=request.POST['uname']
         Password=request.POST['upass']
         CPassword=request.POST['ucpass']
         if userName==''or Password==''or CPassword=='':
             context['errormessage']="Field cannot be blank!!!"
             return render(request,'register.html',context)
         
         elif Password!=CPassword:
             context['errormessage']="Password and confirm password doesnot Match"
             return render(request,'register.html',context)
         
         else:
            try:
                u=User.objects.create(username=userName,password=Password,email=CPassword )
                u.set_password(Password)
                u.save()
                context['successfully']=" User created successfully "
                return render(request,'register.html',context)

            except Exception:
                context['errormessage']="This User Name Alrady Exists!!!"
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')
    
################################# login end #################################################################

from django.http import JsonResponse

def search_suggestions(request):
    query = request.GET.get('q', '').lower()
    suggestions = []

    if query:
################################ processor start ############################################################
        if query in ['i','i3', 'i3 series','intel', 'intel i3']:
            suggestions.append({'name': 'Intel i3 Series', 'url': '/i3_Series/'})

        if query in ['i','i5', 'i5 series','intel', 'intel i5']:
            suggestions.append({'name': 'Intel i5 Series', 'url': '/i5_Series/'})

        if query in ['i','i7', 'i7 series','intel', 'intel i7']:
            suggestions.append({'name': 'Intel i7 Series', 'url': '/i7_Series/'})

        if query in ['i','i9', 'i9 series','intel', 'intel i9']:
            suggestions.append({'name': 'Intel i9 Series', 'url': '/i9_Series/'})

        if query in ['ry','ryz','ryzen','ryzen3', 'ryzen3 series', 'amd ryzen3']:
            suggestions.append({'name': 'AMD Ryzen3 Series', 'url': '/ryzen3/'})

        if query in ['ry','ryz','ryzen','ryzen5', 'ryzen5 series', 'amd ryzen5']:
            suggestions.append({'name': 'AMD Ryzen5 Series', 'url': '/ryzen5/'})

        if query in ['ry','ryz','ryzen','ryzen7', 'ryzen7 series', 'amd ryzen7']:
            suggestions.append({'name': 'AMD Ryzen7 Series', 'url': '/ryzen7/'})

        if query in ['ry','ryz','ryzen','ryzen9', 'ryzen9 series', 'amd ryzen9']:
            suggestions.append({'name': 'AMD Ryzen9 Series', 'url': '/ryzen9/'})

        if query in ['th','thre','thread']:
            suggestions.append({'name': 'AMD Threadripper-Processor Series', 'url': '/Threadripper_Series/'})
            
        if query in ['pro','proces', 'processor']:
            suggestions.append({'name': 'Processor', 'url': '/processorlist/'})

        elif 'processor' in query :
            processors = processor.objects.filter(name__icontains=query)[:5]
            for p in processors:
                suggestions.append({'name': p.card_name, 'url': f'/processors/{p.id}/'})
################################ processor end ##############################################################

################################ motherboard start ##########################################################
        if query in ['m','mo','DD','ddr','ddr5']:
            suggestions.append({'name': 'DDR5 Series', 'url': '/DDR_5/'})
        if query in ['m','mo','th','thre','thread']:
            suggestions.append({'name': 'ThreadRippe Motherboard', 'url': '/ThreadRipper/'})
        if query in ['m','mo','moth','motherb','motherboard']:
            suggestions.append({'name': 'Motherboard 650 series', 'url': '/board_650/'})
        if query in ['m','mo','moth','motherb','motherboard']:
            suggestions.append({'name': 'Motherboard 550 series', 'url': '/board_550/'})
        if query in ['m','mo','moth','motherb','motherboard']:
            suggestions.append({'name': 'Motherboard 450 series', 'url': '/board_450'})
        if query in ['m','mo','moth','motherb','motherboard']:
            suggestions.append({'name': 'Motherboard', 'url': '/motherboardlist/'})

        elif 'motherboard' in query :
            motherboards = motherboard.objects.filter(name__icontains=query)[:5]
            for m in motherboards:
                suggestions.append({'name': m.card_name, 'url': f'/motherboards/{m.id}/'})
################################ motherboard end #############################################################

################################ graphiccard start ###########################################################
        if query in ['g','ga','gar','grap','grapcar']:
            suggestions.append({'name': 'Grapcard 1650 series', 'url': '/Cards_1650/'})
        if query in ['g','ga','gar','grap','grapcar']:
            suggestions.append({'name': 'Grapcard 3050 series', 'url': '/Cards_3050/'})
        if query in ['g','ga','gar','grap','grapcar']:
            suggestions.append({'name': 'Grapcard 3050 series', 'url': '/Cards_4060/'})
        if query in ['g','ga','gar','grap','grapcar']:
            suggestions.append({'name': 'Grapcard series', 'url': '/grapcardlist/'})

        elif 'graphic card' in query :
            graphiccards = graphiccard.objects.filter(name__icontains=query)[:5]
            for g in graphiccards:
                suggestions.append({'name': g.card_name, 'url': f'/graphiccards/{g.id}/'})
################################ graphiccard end ############################################################

################################ cooling start ##############################################################
        if query in ['c','co','cooli']:
            suggestions.append({'name': 'Cooler 120mm', 'url': '/Cooler_120mm/'})
        if query in ['c','co','cooli']:
            suggestions.append({'name': 'Cooler 240mm', 'url': '/Cooler_240mm/'})
        if query in ['c','co','cooli']:
            suggestions.append({'name': 'Cooler 300mm', 'url': '/Cooler_300mm/'})
        if query in ['c','co','cooli']:
            suggestions.append({'name': 'CPU RGB Coole', 'url': '/CPU_RGB_Coole/'})
        if query in ['c','co','cooli']:
            suggestions.append({'name': 'Custom RGB Cooler', 'url': '/Custom_RGB_Cooler/'})
        if query in ['c','co','cooli']:
            suggestions.append({'name': 'coolingsystem', 'url': '/coolingsystemdlist/'})

        elif 'cooling' in query :
            coolingsystems = coolingsystem.objects.filter(name__icontains=query)[:5]
            for c in coolingsystems:
                suggestions.append({'name': c.card_name, 'url': f'/coolingsystems/{c.id}/'})
################################ cooling end ################################################################

################################ ram start ##################################################################
        if query in ['r','ra','ram']:
            suggestions.append({'name': 'Ram 8GB', 'url': '/Ram_8GB/'})
        if query in ['r','ra','ram']:
            suggestions.append({'name': 'Ram 16GB', 'url': '/Ram_16GB/'})
        if query in ['r','ra','ram']:
            suggestions.append({'name': 'Ram 32GB', 'url': '/Ram_32GB/'})
        if query in ['r','ra','ram']:
            suggestions.append({'name': 'Ram 64GB', 'url': '/Ram_64GB/'})
        if query in ['r','ra','ram']:
            suggestions.append({'name': 'RAM', 'url': '/ramlist/'})

        elif 'ram' in query :
            rams = ram.objects.filter(name__icontains=query)[:5]
            for r in rams:
                suggestions.append({'name': r.card_name, 'url': f'/ram/{r.id}/'})
################################ ram end ###################################################################

################################ ssd start #################################################################
        if query in ['s','ss','ssd','256GB series']:
            suggestions.append({'name': 'SSD 256GB', 'url': '/ssd_256GB/'})
        if query in ['s','ss','ssd','500GB series']:
            suggestions.append({'name': 'SSD 500GB', 'url': '/ssd_500GB/'})
        if query in ['m.2','m.2 nv','m.2 nvme ']:
            suggestions.append({'name': 'M.2 NVMe 256GB', 'url': '/M_2_NVMe_256GB/'})
        if query in ['m.2','m.2 nv','m.2 nvme ', 'm.2 nvme 500']:
            suggestions.append({'name': 'M.2 NVMe 500GB', 'url': '/M_2_NVMe_500GB/'})
        if query in ['m.2','m.2 nv','m.2 nvme ', 'm.2 nvme 1']:
            suggestions.append({'name': 'M.2 NVMe 1TB', 'url': '/M_2_NVMe_1TB/'})
        if query in ['ss','ssd','inter','internal ssd']:
            suggestions.append({'name': 'Internal SSD', 'url': '/ssdlist/'})

        elif 'ssd' in query :
            ssds = ssd.objects.filter(name__icontains=query)[:5]
            for s in ssds:
                suggestions.append({'name': s.card_name, 'url': f'/ssds/{s.id}/'})
################################ ssd end ###################################################################

################################ smps start ################################################################
        if query in ['sm','smps','smps 400w']:
            suggestions.append({'name': 'SMPS 400W', 'url': '/smbs_400W/'})
        if query in ['sm','smps','smps 500w']:
            suggestions.append({'name': 'SMPS 500W', 'url': '/smbs_500W/'})
        if query in ['sm','smps','smps 600w']:
            suggestions.append({'name': 'SMPS 600W', 'url': '/smbs_600W/'})
        if query in ['sm','smps','smps 800W']:
            suggestions.append({'name': 'SMPS 800W', 'url': '/smbs_800W/'})
        if query in ['sm','smps','smps 1000w']:
            suggestions.append({'name': 'SMPS 1000W', 'url': '/smbs_1000w/'})
        if query in ['sm','smps','smps']:
            suggestions.append({'name': 'SMPS For PC', 'url': '/smbslist/'})

        elif 'smps' in query :
        # elif 'smps' in query or query.startswith('sm') or query.startswith('smp'):
            smps = smbs.objects.filter(name__icontains=query)[:5]
            for sm in smps:
                suggestions.append({'name': sm.card_name, 'url': f'/smbs/{sm.id}/'})
################################ smps end ##################################################################
    return JsonResponse(suggestions, safe=False)

def search_results(request):
    query = request.GET.get('q', '').lower()
################################ processor start ###########################################################
    if query in ['i3 series']:
        return redirect('i3_Series')
    if query in ['i5 series']:
        return redirect('i5_Series')
    if query in ['i7 series']:
        return redirect('i7_Series')
    if query in ['i9 series']:
        return redirect('i9_Series')
    if query in ['ryzen3 series']:
        return redirect('ryzen3/')
    if query in ['ryzen5 series']:
        return redirect('ryzen5/')
    if query in ['ryzen7 series']:
        return redirect('ryzen7/')
    if query in ['ryzen9 series']:
        return redirect('ryzen9/')
    if query in ['thread']:
        return redirect('Threadripper_Series/')
    if query in ['processorlist']:
        return redirect('processorlist/')   
################################ processor end ##############################################################

################################ motherboard start ##########################################################
    if query in ['DDR5 series']:
        return redirect('DDR_5/')
    if query in ['thread']:
        return redirect('ThreadRipper/')
    if query in ['650 series']:
        return redirect('board_650/')
    if query in ['550 series']:
        return redirect('board_550/')
    if query in ['450 series']:
        return redirect('board_450/')
    if query in ['motherboardlist']:
        return redirect('motherboardlist/')
################################ motherboard end #############################################################

################################ graphiccard start ###########################################################
    if query in ['1650 series']:
        return redirect('Cards_1650/')
    if query in ['3050 series']:
        return redirect('Cards_3050/')
    if query in ['4060 series']:
        return redirect('Cards_4060/')
    if query in ['graphiccardlist']:
        return redirect('graphiccardlist/')
################################ graphiccard end #############################################################

################################ cooling start ###############################################################
    if query in ['120mm series']:
        return redirect('Cooler_120mm/')
    if query in ['240mm series ']:
        return redirect('Cooler_240mm/')
    if query in ['300mm series']:
        return redirect('Cooler_300mm/')
    if query in ['CPU_RGB_Coole']:
        return redirect('CPU_RGB_Coole/')
    if query in ['Custom_RGB_Cooler']:
        return redirect('Custom_RGB_Cooler/')
    if query in ['coolingsystemdlist']:
        return redirect('coolingsystemdlist/')
################################ cooling end #################################################################

################################ ram start ###################################################################
    if query in ['Ram_8GB']:
        return redirect('Ram_8GB/')
    if query in ['Ram_16GB ']:
        return redirect('Ram_16GB/')
    if query in ['Ram_32GB']:
        return redirect('Ram_32GB/')
    if query in ['Ram_64GB']:
        return redirect('Ram_64GB/')
    if query in ['ramlist']:
        return redirect('ramlist/')
################################ ram end #####################################################################

################################ ssd start ###################################################################
    if query in ['ssd_256GB']:
        return redirect('ssd_256GB/')
    if query in ['ssd_500GB']:
        return redirect('ssd_500GB/')
    if query in ['M_2_NVMe_256GB']:
        return redirect('M_2_NVMe_256GB/')
    if query in ['M_2_NVMe_500GB']:
        return redirect('M_2_NVMe_500GB/')
    if query in ['M_2_NVMe_1TB']:
        return redirect('M_2_NVMe_1TB/')
    if query in ['ssdlist']:
        return redirect('ssdlist/')
################################ ssd end #####################################################################

################################ smps start ##################################################################
    if query in ['smbslist']:
        return redirect('smbslist/')
    if query in ['smbs_400W']:
        return redirect('smbs_400W/')
    if query in ['smbs_500W']:
        return redirect('smbs_500W/')
    if query in ['smbs_600W']:
        return redirect('smbs_600W/')
    if query in ['smbs_800W']:
        return redirect('smbs_800W/')
    if query in ['smbs_1000w']:
        return redirect('smbs_1000w/')
################################ smps end ####################################################################

    processors, motherboards, graphiccards, coolingsystems, rams, ssds, smps = [], [], [], [], [], [], []

    if query:
        if 'processor' in query or query.startswith('p') or query.startswith('pr'):
            processors = processor.objects.filter(name__icontains=query)
        elif 'motherboard' in query or query.startswith('m'):
            motherboards = motherboard.objects.filter(name__icontains=query)
        elif 'graphic card' in query or query.startswith('g'):
            graphiccards = graphiccard.objects.filter(name__icontains=query)
        elif 'cooling' in query or query.startswith('c'):
            coolingsystems = coolingsystem.objects.filter(name__icontains=query)
        elif 'ram' in query or query.startswith('r'):
            rams = ram.objects.filter(name__icontains=query)
        elif 'ssd' in query or query.startswith('s'):
            ssds = ssd.objects.filter(name__icontains=query)
        elif 'smps' in query:
            smps = smbs.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'processors': processors,
        'motherboards': motherboards,
        'graphiccards': graphiccards,
        'coolingsystems': coolingsystems,
        'ram': rams,
        'ssds': ssds,
        'smbsp': smps,
    }
    return render(request, 'search_results.html', context)
