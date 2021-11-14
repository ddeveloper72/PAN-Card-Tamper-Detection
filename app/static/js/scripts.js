// Wait for the DOM to be ready
$(document).ready(function () {
    //  replace the data text with the new name of the Pan Card selected
    $("form").on("change", ".file-upload-field", function () {
        $(this).parent(".file-upload-wrapper").attr("data-text", $(this).val().replace(/.*(\/|\\)/, ''));
        $('#result').show();
    });

    // file type validation
    $('INPUT[type="file"]').change(function () {
        var ext = this.value.match(/\.(.+)$/)[1];
        switch (ext) {
            // sepcify the file extension our code works with.
            case 'jpg':
                break;
            default:
                alert('Sorry, only jpg files are allowed.');
        }
    });

    // Initialize form validation on the Pan Card form.
    // It has the name attribute "registration"
    $("form[name='PanCardUpload']").validate({
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            file_upload: "required",
        },
        // Specify validation error messages
        messages: {
            file_upload: "Please select a Pan Card",
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function (form) {
            form.submit();
        }
    });

});
