window.revelar = ScrollReveal ({reset: true})

revelar.reveal('.imagem-comp1',{
    duration:1000,
    origin:'right',
    distance: '100px',
    delay: 500,
    reset: false
}); 
revelar.reveal('.texto-comp1',{
    duration:1000,
    origin:'right',
    distance: '200px',
    delay: 1000,
    reset: false
}); 



function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            // Certifique-se de que o elemento com id 'file_upload' é uma imagem
            var fileUpload = document.getElementById('file_upload');
            if (fileUpload) {
                fileUpload.src = e.target.result;
            } else {
                console.error('Elemento com id "file_upload" não encontrado.');
            }
        };
        reader.onerror = function (error) {
            console.error('Erro ao ler o arquivo: ', error);
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        console.error('Nenhum arquivo selecionado.');
    }
}