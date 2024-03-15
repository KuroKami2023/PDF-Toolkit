const { PythonShell } = require('python-shell');

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("pdf-upload-form");
    const messageDiv = document.getElementById("conversion-msg");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const pdfFile = document.getElementById("pdf-file").files[0];
        if (!pdfFile) {
            showMessage("Please select a PDF file.");
            return;
        }

        // Create PythonShell object to run the Python script
        const options = {
            mode: 'text',
            pythonOptions: ['-u'], // unbuffered output
            scriptPath: __dirname, // current directory
            args: [pdfFile.path] // send PDF file path as an argument
        };

        PythonShell.run('pdf_to_excel.py', options, function (err, results) {
            if (err) {
                showMessage("Error: " + err);
            } else {
                showMessage("Conversion successful.");
            }
        });
    });

    function showMessage(message) {
        messageDiv.innerText = message;
    }
});
