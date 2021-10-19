const ham = document.getElementById('burger');
    const navUl = document.getElementById('nav-ul');
    
    ham.addEventListener('click', () => {
        navUl.classList.toggle('show');

    });