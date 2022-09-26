// let post = document.getElementsByClassName('post')
// let post__button = document.getElementsByClassName('post__button')

    
// for(let button of post__button){
//     button.addEventListener('click', (e)=>{        
//         item_img = e.target.parentElement.children[0].currentSrc
//         item_title = e.target.parentElement.children[1].textContent
//         item_price = e.target.parentElement.children[2].children[0].textContent
//         item_price = parseFloat(item_price)
//         cantidad = 1
//         total = item_price*cantidad
//         item = {
//             img: item_img,
//             title: item_title,
//             item_price: item_price,
//             cantidad: cantidad,
//             total: total
//         }
//         if(localStorage.getItem(item_title) == null){
//             localStorage.setItem(item_title, JSON.stringify(item))
//         }else{
//            item_modificar = JSON.parse(localStorage.getItem(item_title))
//            item_modificar.cantidad += 1
//            localStorage.setItem(item_title, JSON.stringify(item_modificar))
//         }
//     })
// }


