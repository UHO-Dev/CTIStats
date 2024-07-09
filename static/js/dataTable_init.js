$(document).ready(function(){
    var table = $('#example').DataTable({
        orderCellsTop: true,
        fixedHeader: true,        
        language: {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        },
    });
});

/*$('#example thead tr').clone(true).appendTo('#example thead');

$('#example thead tr:eq(1) th').each(function(i){
    var title = $(this).text();
    $(this).html('<input type="text" placeholder="buscar '+title+'">');

    $('input', this).on('keyup change',function(){
        if (table.column(i).search() !== this.value){
            table
                .column(i)
                .search(this.value)
                .draw();
        }
    });
});*/