const menu = document.getElementById('iconemenu')
const  ul = document.getElementById('ulmenu')

menu.addEventListener('click', ()=>{
    if (ul.style.display == 'none'){
        ul.style.display = 'flex'
        menu.src = "static/img/blogIcons/menu_close.png"
    }else{
        ul.style.display = 'none'
        menu.src = "static/img/blogIcons/menu.png"
    }
})