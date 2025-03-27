async function uploadDocuments() {
    const fileInput = document.getElementById('uploadFile');
    const fileList = document.getElementById('documentList');
    const files = fileInput.files;

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append('file', files[i]);
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/upload/', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();
        
        for (let i = 0; i < files.length; i++) {
            const li = document.createElement('li');
            li.textContent = files[i].name;
            fileList.appendChild(li);
        }
        
        // Aggiungi messaggio di conferma
        const successMessage = document.createElement('p');
        successMessage.textContent = `File caricato con successo: ${result.filename}`;
        successMessage.style.color = 'green';
        document.querySelector('#documenti').appendChild(successMessage);
        
        // Rimuovi il messaggio dopo 3 secondi
        setTimeout(() => successMessage.remove(), 3000);
        
        console.log("Risposta dal server:", result);
    } catch (error) {
        console.error("Errore durante il caricamento:", error);
        // Messaggio di errore
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'Errore durante il caricamento.';
        errorMessage.style.color = 'red';
        document.querySelector('#documenti').appendChild(errorMessage);
        setTimeout(() => errorMessage.remove(), 3000);
    }
}