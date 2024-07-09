function filterByYear() {
    var year = document.getElementById("year").value;
    
    // Filtrar la lista con JavaScript
    var filteredList = lista.filter(function(item) {
      return item.fecha.includes(year); 
    });
  
    // Renderizar la lista filtrada
    renderList(filteredList);
  }

  function renderList(list) {
    // Lógica para renderizar la tabla con la lista filtrada
  } 