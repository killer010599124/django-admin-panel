window.addEventListener("load", function() {

    var flug1 = document.getElementById("id_flug1");
    var flug2 = document.getElementById("id_flug2");
    var flug3 = document.getElementById("id_flug3");
    var flug4 = document.getElementById("id_flug4");
    var flug5 = document.getElementById("id_flug5");
    var flug6 = document.getElementById("id_flug6");
    var flug7 = document.getElementById("id_flug7");
    flug1.disabled=true;
    flug2.disabled=true;
    flug3.disabled=true;
    flug4.disabled=true;
    flug5.disabled=true;
    flug6.disabled=true;
    flug7.disabled=true;
    var temp_flug = {
        'flug1': flug1.value,
        'flug2': flug2.value,
        'flug3': flug3.value,
        'flug4': flug4.value,
        'flug5': flug5.value,
        'flug6': flug6.value,
        'flug7': flug7.value
    };

    (function($) {
        $('a[id^="flug_button"]').click(function() {
            var buttonId = $(this).attr('id');
            var id = buttonId.charAt(buttonId.length - 1);
            console.log('flug ID: ' + id );

            var extra = document.getElementById("id_flug_extra" + id);

            var url = $("#flug_url").attr("data-url");
            console.log(url);

            $.ajax({
                data: {'extra': extra.value}, // get the form data
                url: url,
                // on success
                success: function (response) {
                    var flug = document.getElementById("id_flug"+ id);
                    flug.value = response.id;

                    console.log(flug.value);
                },
                // on error
                error: function (response) {
                    console.log(response.responseJSON.errors);
                }
            });
            return false;
        });

        $('input[id^="id_verkehr_extra"]').change(function() {
            var buttonId = $(this).attr('id');
            var id = buttonId.charAt(buttonId.length - 1);
            console.log('verkehr ID: ' + id );

            var url = $("#verkehr_url").attr("data-url");
            console.log(url);

            $.ajax({
                data: {'extra': this.value}, // get the form data
                url: url,
                // on success
                success: function (response) {
                    var verkehr = document.getElementById("id_verkehr"+ id);
                    verkehr.value = response.id;

                    console.log(verkehr.value);
                },
                // on error
                error: function (response) {
                    console.log(response.responseJSON.errors);
                }
            });
            return false;
        });

        $('input[id^="id_flug_save"]').change(function(event) {
            var buttonId = $(this).attr('id');
            var id = buttonId.charAt(buttonId.length - 1);
            console.log('flug ID: ' + id );

            var flug = document.getElementById("id_flug"+ id);
            flug.disabled = !this.checked;

            if(!this.checked){
                flug.value = temp_flug["flug"+ id];
            }
        });


        //Hide button Label
        $('div[class^="fieldBox"][class$="_button"]').find('label[class="inline"]').hide();

        //Hide the other field label
        $('label[for^="id_flug_save"]').hide();
        $('label[for^="id_flug_extra"]').hide();
        $('label[for^="id_verkehr_extra"]').hide();

        //Hide id text_fields
        $('input[type="number"][name^="flug"]').hide();
        $('input[type="number"][name^="verkehr"]').hide();

    })(django.jQuery);
});