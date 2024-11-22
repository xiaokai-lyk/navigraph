// Function to fetch options for the dropdowns
async function loadOptions() {
    try {
        // Sending POST request to fetch options
        const response = await fetch('/api/nodes_i', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        });

        if (response.status != 200) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Populate dropdown menus with the received data
        populateDropdown('target', data);
    } catch (error) {
        console.error('Error loading options:', error);
    }
    //INITIAL EMPTY MAP
    try {
        const response = await fetch('/api/internalNavi', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'

            },
            body: JSON.stringify({ building: "Aspiration Building", target: 0 })
        });

        if (response.status == 200) {
            const data = await response.json();
            if (data && data.image_base64) {
                // Update the image element with Base64 data
                const resultImage = document.getElementById('resultImage');
                resultImage.src = `data:image/png;base64,${data.image_base64}`; // Set base64 data as source
                resultImage.style.display = 'block'; // Make the image visible
            } else {
                console.error('No image_base64 in response:', data);
            }
        } else {
            console.error('Error submitting form:', response.statusText);
        }
    } catch (error) {
        console.error('Error submitting form:', error);
    }
}

// Helper function to populate dropdowns
function populateDropdown(elementId, options) {
    const dropdown = document.getElementById(elementId);
    dropdown.innerHTML = ''; // Clear existing options

    if (Array.isArray(options)) {
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option.value; // Assuming the API provides { value: "", label: "" }
            opt.textContent = option.label;
            dropdown.appendChild(opt);
        });
    } else {
        const opt = document.createElement('option');
        opt.value = '';
        opt.textContent = 'No options available';
        dropdown.appendChild(opt);
    }
}

// Handle form submission
window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('dropdownForm').addEventListener('submit', async (event) => {
        event.preventDefault();
        const buildingName = document.getElementById('building').value;
        const targetValue = document.getElementById('target').value;
        console.log("loading navigation")
        try {
            const response = await fetch('/api/internalNavi', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'

                },
                body: JSON.stringify({ building: "Aspiration Building", target: targetValue })
            });

            if (response.status == 200) {
                const r = await response.text();
                try {
                    const data = JSON.parse(r);
                    if (data && data.image_base64) {
                        // Update the image element with Base64 data
                        const resultImage = document.getElementById('resultImage');
                        resultImage.src = `data:image/png;base64,${data.image_base64}`; // Set base64 data as source
                        resultImage.style.display = 'block'; // Make the image visible
                    } else {
                        console.error('No image_base64 in response:', data);
                    }
                }
                catch (error) {
                    document.getElementById('errorRes').innerHTML = r;
                    document.getElementById('wrapper').style.display = 'none';
                }
            } else {
                console.error('Error submitting form:', response.statusText);
            }
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    });
});

// Load options on page load
window.addEventListener('DOMContentLoaded', () => {
    console.log('Loading options...');
    loadOptions();
});