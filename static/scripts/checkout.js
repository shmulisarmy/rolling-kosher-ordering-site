function loadItems() {
  const items_input = document.querySelector('input[name="items"]');
  items_input.value = localStorage.getItem('items');
}