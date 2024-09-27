
// State-to-city and city-to-pin code mapping
const stateCityMap = {
    "Tamil Nadu": {
        cities: ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
        pins: [
            ["600001", "600002", "600003", "600004", "600005", "600006", "600007", "600008", "600009", "600010", "600011", "600012", "600013", "600014", "600015", "600016", "600017", "600018", "600019", "600020", "600021", "600022", "600023", "600024", "600025", "600026", "600027", "600028", "600029", "600030", "600031", "600032", "600033", "600034", "600035", "600036", "600037", "600038", "600039", "600040", "600041", "600042", "600043", "600044", "600045", "600046", "600047", "600048", "600049", "600050"],  // Chennai
            ["641001", "641002", "641003"],  // Coimbatore
            ["625001", "625002", "625003"],  // Madurai
            ["620001", "620002", "620003"],  // Tiruchirappalli
            ["636001", "636002", "636003"]   // Salem
        ]
    },
    "Kerala": {
        cities: ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kannur"],
        pins: [
            ["695001", "695002", "695003"],  // Thiruvananthapuram
            ["682001", "682002", "682003"],  // Kochi
            ["673001", "673002", "673003"],  // Kozhikode
            ["680001", "680002", "680003"],  // Thrissur
            ["670001", "670002", "670003"]   // Kannur
        ]
    }
};

// Handle state selection
document.getElementById("state").addEventListener("change", function () {
    const selectedState = this.value;
    const citySelect = document.getElementById("city");
    const zipcodeSelect = document.getElementById("zipcode");

    // Clear the city dropdown and reset pin code dropdown
    citySelect.innerHTML = '<option value="" disabled selected>Select your city</option>';
    zipcodeSelect.innerHTML = '<option value="" disabled selected>Select your pin code</option>';

    // Populate city options based on selected state
    if (selectedState in stateCityMap) {
        stateCityMap[selectedState].cities.forEach(function (city, index) {
            const option = document.createElement("option");
            option.value = city;
            option.text = city;
            option.setAttribute("data-pins", JSON.stringify(stateCityMap[selectedState].pins[index])); // Store pin codes in data attribute
            citySelect.appendChild(option);
        });
    }
});

// Handle city selection to update pin codes
document.getElementById("city").addEventListener("change", function () {
    const selectedCity = this.options[this.selectedIndex];
    const pinCodes = JSON.parse(selectedCity.getAttribute("data-pins"));
    const zipcodeSelect = document.getElementById("zipcode");

    // Clear the pin code dropdown
    zipcodeSelect.innerHTML = '<option value="" disabled selected>Select your pin code</option>';

    // Populate pin code options based on selected city
    pinCodes.forEach(function (pin) {
        const option = document.createElement("option");
        option.value = pin;
        option.text = pin;
        zipcodeSelect.appendChild(option);
    });
});

// Optionally, you can preselect values from initial_data if available
window.onload = function () {
    const initialState = "{{ initial_data.state }}";
    const initialCity = "{{ initial_data.city }}";
    const initialZip = "{{ initial_data.zipcode }}";

    if (initialState) {
        document.getElementById("state").value = initialState;
        document.getElementById("state").dispatchEvent(new Event('change'));

        if (initialCity) {
            document.getElementById("city").value = initialCity;
            document.getElementById("city").dispatchEvent(new Event('change'));

            if (initialZip) {
                document.getElementById("zipcode").value = initialZip;
            }
        }
    }
};
