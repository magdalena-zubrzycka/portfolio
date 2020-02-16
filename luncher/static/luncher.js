

$('input.potrawy-wybor').change(function() {
    var zaznaczone_zupy = $("input.potrawy-wybor[data-typ='1']:checked");
    var zaznaczone_dania = $("input.potrawy-wybor[data-typ='2']:checked");
    var zaznaczone_extra = $("input.potrawy-wybor[data-typ='3']:checked");
    if (zaznaczone_extra.length > 0){
        $("input.potrawy-wybor:not(:checked)").attr("disabled", true).closest('.wybor-dania').addClass('brak_wyboru');
    } else if(zaznaczone_dania.length >0 && zaznaczone_zupy.length ==0 ){
        $("input.potrawy-wybor[data-typ!='1']:not(:checked)").attr("disabled", true).closest('.wybor-dania').addClass('brak_wyboru');
        $("input.potrawy-wybor[data-typ='1']:not(:checked)").attr("disabled", false).closest('.wybor-dania').removeClass('brak_wyboru');
    } else if(zaznaczone_dania.length >0 && zaznaczone_zupy.length >0 ){
        $("input.potrawy-wybor:not(:checked)").attr("disabled", true).closest('.wybor-dania').addClass('brak_wyboru');
    } else if(zaznaczone_dania.length == 0 && zaznaczone_zupy.length > 0 ){
        $("input.potrawy-wybor[data-typ!='2']:not(:checked)").attr("disabled", true).closest('.wybor-dania').addClass('brak_wyboru');
        $("input.potrawy-wybor[data-typ='2']:not(:checked)").attr("disabled", false).closest('.wybor-dania').removeClass('brak_wyboru');
    } else {
        $("input.potrawy-wybor").attr("disabled", false).closest('.wybor-dania').removeClass('brak_wyboru');
    }
});

$('.row.wybor-dania').click(function(event){
    var boxy = $(this).find('input.potrawy-wybor');
    if (event.target != boxy[0]){
        boxy.click();
    }
});

$('#exampleModal').on('show.bs.modal', function (event) {
    var wiersze = $("input.potrawy-wybor:checked").closest('.wybor-dania');
    var modal = $(this);
    for(var i=0; i < wiersze.length; i++) {
        var opis = $(wiersze[i]).find('.danie-opis');
        modal.find('.potwierdzanie-zamowienia:nth-child(' + (i+1) + ")").html(opis);
    }
});
