function loadItems() {
  const items_input = document.querySelector('input[name="items"]');
  items_input.value = localStorage.getItem('items');
}

function showDialog() {
    const dialog = document.querySelector('dialog');
    dialog.show();
    console.log("updated")
    document.querySelector('body').classList.add('model-open');
}
