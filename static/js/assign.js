const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");


nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        }
    })
})

backBtn.addEventListener("click", () => form.classList.remove('secActive'));



function toggleAdditionalServices() {
    const needAdditionalServices = document.getElementById('need_additional_services').value;
    const servicesContainer = document.getElementById('services-container');
    if (needAdditionalServices === 'yes') {
        servicesContainer.style.display = 'block';
    } else {
        servicesContainer.style.display = 'none';
    }
}

function addMedicine() {
    const container = document.getElementById('medicines-container');
    const newEntry = document.createElement('div');
    newEntry.classList.add('medicine-entry');
    newEntry.innerHTML = `        
        <label for="medicine">Select Medicine:</label>
        <select name="medicine_id[]" id="medicine" class="form-control">
            {% for medicine in medicines %}
                <option value="{{ medicine.id }}">{{ medicine.name }} - ${{ medicine.price }}</option>
            {% endfor %}
        </select>
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity[]" value="1" min="1" class="form-control">
        <label for="time">Medicine Time:</label>
        <input type="text" id="time" name="time[]" placeholder="e.g., 1-0-1" class="form-control">
        <hr>
    `;
    container.appendChild(newEntry);
}

function toggleRoomAllocation() {
    const needAdmit = document.getElementById('need_admit').value;
    const roomAllocation = document.getElementById('room-allocation');
    if (needAdmit === 'yes') {
        roomAllocation.style.display = 'block';
    } else {
        roomAllocation.style.display = 'none';
    }
}

function addService() {
    const container = document.getElementById('services-container');
    const newEntry = document.createElement('div');
    newEntry.classList.add('service-entry');
    newEntry.innerHTML = `
        <label for="service_name">Service Name:</label>
        <input type="text" name="service_name[]" id="service_name">
        <br><br>
        <label for="service_quantity">Quantity:</label>
        <input type="number" name="service_quantity[]" id="service_quantity" value="1" min="1">
        <br><br>
        <label for="service_price">Price:</label>
        <input type="number" name="service_price[]" id="service_price" step="0.01" min="0">
        <hr>
    `;
    container.appendChild(newEntry);
}

