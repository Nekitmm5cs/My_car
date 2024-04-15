document.getElementById('openBtn').addEventListener('click', function() {
    document.querySelector('.modal-overlay').style.display = 'flex';
});

document.querySelector('.close').addEventListener('click', function() {
    document.querySelector('.modal-overlay').style.display = 'none';
});

document.getElementById('nextBtn').addEventListener('click', function() {
    document.querySelector('.modal-content:not(.hidden)').classList.add('hidden');
    document.querySelector('.modal-content:not(.hidden) + .modal-content').classList.remove('hidden');
});

document.getElementById('prevBtn').addEventListener('click', function() {
    document.querySelector('.modal-content:not(.hidden)').classList.add('hidden');
    document.querySelector('.modal-content:not(.hidden):last-of-type').classList.remove('hidden');
});
