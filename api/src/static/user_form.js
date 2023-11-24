function validateForm() {
    var checkboxes = document.querySelectorAll('input[name="door_access"]:checked');
    if (checkboxes.length == 0) {
        alert('Lütfen en az bir seçim yapın.');
        return false;
    }
    return true;
}

function toggleCheckbox(checkbox) {
    checkbox.checked = !checkbox.checked;
    var container = checkbox.closest('.checkbox-container');
    container.classList.toggle('checked', checkbox.checked);
    container.style.backgroundColor = checkbox.checked ? '#b3e5fc' : '#f8f8f8';
}

var checkboxContainers = document.querySelectorAll('.checkbox-container');
checkboxContainers.forEach(function (container) {
    var checkbox = container.querySelector('input[type="checkbox"]');
    container.addEventListener('click', function () {
        toggleCheckbox(checkbox);
    });
});



function searchCheckboxes() {
    var searchText = document.getElementById('searchText').value.toLowerCase();
    var checkboxContainers = document.querySelectorAll('.checkbox-container');

    checkboxContainers.forEach(function (container) {
        var label = container.querySelector('label');
        var labelText = label.textContent.toLowerCase();

        if (labelText.includes(searchText)) {
            container.style.display = 'block';
        } else {
            container.style.display = 'none';
        }
    });
}