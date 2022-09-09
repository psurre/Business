/**
 * 
 * Configuration du bouton top
 * Language : JQuery
 */
function animateButtonTop() {
    // Display
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    // Scroll to top
    $('#back-to-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
    });
}

/**
 * 
 * Initialise les collapsible pour que l'action lors du clic fonctionne
 * Language : JS
 */
function initializeCollapsibles() {
    // Initialisation des collapsible 
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
}


/**
 * 
 * Alterne 1 fois sur 2 la couleur d'arrière plan des sections'
 * Language : JQuery
 */
function initializeSectionsBackground() {
    var i = 0;
    $('section').each(function () {
        if (i % 2 == false)
            $(this).addClass("light-bg");
        i++;
    });
}

function enableTooltipEverywhere() {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });
}
function AddFontAwesomeIcon(item, icon) {
    item.classList.add("fas");
    item.classList.add(icon);
}
/**
 * Exécuté lorsque la page est chargée (Comme une fonction Main)
 * Language : JQuery
 */
$(document).ready(function () {
    // Initialisation du Modal
    $('#modal-popup').modal('show');

    // Initialisation du Calendrier pour le Modal
    $("#datepicker").datepicker({
        minDate: 1
    });

    animateButtonTop();
    initializeCollapsibles();
    // Désactivé jusqu'à nouvel ordre (pour que le rendu reste joli, en effet, le fond blanc des images est visible sur le fond light-bg)
    initializeSectionsBackground();
    enableTooltipEverywhere();
});