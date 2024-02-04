// static/js/script.js
document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.querySelector('.menu-btn');
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    const header = document.querySelector('.header');
    console.log('javasc',header, menuBtn, sidebar, content)

    if (menuBtn && sidebar && content) {
        menuBtn.addEventListener('click', function () {
        console.log('Button clicked!');
            const sidebarWidth = getComputedStyle(sidebar).width;

            if (sidebarWidth === '250px') {
                sidebar.style.width = '0';
                content.style.marginLeft = '0';
                header.style.marginLeft = '0';
            } else {
                sidebar.style.width = '250px';
                content.style.marginLeft = '250px';
                header.style.marginLeft = '250px';
            }
        });
    }
     // Close sidebar when an item is clicked
    const sidebarItems = document.querySelectorAll('.sidebar a');
    sidebarItems.forEach(item => {
        item.addEventListener('click', function () {
            sidebar.style.width = '0';
            content.style.marginLeft = '0';
        });
    });
});
