$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $('#content-wrapper').toggleClass('toggled');
});

$(document).ready(function() {
    $('#datatable-programmers').DataTable({
        language: {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 a 0 de 0 Entradas",
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
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        },buttons: [
            {
                extend: 'pdf', // Agrega el botón de exportación a Excel
                text: 'Exportar a PDF', // Texto del botón
                className: 'buttons-pdf', // Clase CSS del botón
                id: 'export-pdf' // Identificador único del botón
            },
            {
                extend: 'excel', // Agrega el botón de exportación a Excel
                text: 'Exportar a Excel', // Texto del botón
                className: 'buttons-excel', // Clase CSS del botón
                id: 'export-excel' // Identificador único del botón
            },
            {
                extend: 'csv', // Agrega el botón de exportación a CSV
                text: 'Exportar a CSV', // Texto del botón
                className: 'buttons-csv', // Clase CSS del botón
                id: 'export-csv' // Identificador único del botón
            }
        ],
        initComplete: function() {
            this.api().columns().every(function() {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($(column.footer()).empty())
                    .on('change', function() {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
    
                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });
    
                column.data().unique().sort().each(function(d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>');
                });
            });
        }
    });
    

    $('#export-pdf').on('click', function() {
        $('#datatable-programmers').DataTable().button('.buttons-pdf').trigger();
    });

    $('#export-excel').on('click', function() {
        $('#datatable-programmers').DataTable().button('.buttons-excel').trigger();
    });

    $('#export-csv').on('click', function() {
        $('#datatable-programmers').DataTable().button('.buttons-csv').trigger();
    });
});

            




function resaltarBusqueda() {
    // Obtener el valor del campo de búsqueda
    var searchTerm = $('#search-form input[type="search"]').val().toLowerCase();

    // Eliminar cualquier resaltado anterior
    $('.highlighted').removeClass('highlighted');

    // Buscar y resaltar la palabra en el texto visible
    $('body').find(':not(script)').contents().filter(function() {
        return this.nodeType === 3 && this.textContent.toLowerCase().includes(searchTerm);
    }).each(function() {
        var $parent = $(this).parent();
        var text = this.textContent;
        var regex = new RegExp(searchTerm, 'gi');
        var highlightedText = text.replace(regex, '<span class="highlighted">$&</span>');
        $parent.html($parent.html().replace(text, highlightedText));
    });

    // Desplazarse a la primera aparición de la palabra buscada
    var $firstHighlighted = $('.highlighted').first();
    if ($firstHighlighted.length > 0) {
        $('html, body').animate({
            scrollTop: $firstHighlighted.offset().top
        }, 500);
    }
}