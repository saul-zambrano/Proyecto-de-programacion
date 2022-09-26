// let table_body = document.getElementById('tb-body')


// /* Insertar datos en el carrito de compra */

// const insertShopping = () =>{
//     let fragment = document.createDocumentFragment()

//     for(let i = 0; i< localStorage.length; i++){
//         let item = JSON.parse(localStorage.getItem(localStorage.key(i)))
//         let tr = document.createElement('TR')
//         let td_1 = document.createElement('TD')
//         let td_2 = document.createElement('TD')
//         let td_3 = document.createElement('TD')
//         let td_4 = document.createElement('TD')
//         tr.setAttribute('class', 'tbody-product__row')
//         td_1.innerHTML = 
//         `<div class="tbody-product__images">
//             <img src="${item.img}" alt="">
//         </div>`
//         td_2.innerHTML = 
//         `<a href="">${item.title}</a>
//         <p>Precio: $${item.item_price}</p>
//         `
//         td_3.innerHTML = 
//         `<input class="row__input" type="number" min="1" max="100" value="${item.cantidad}"></input>
//         <button type="" class="removeElement">Eliminar</button>
//         `
//         td_4.innerHTML = 
//         `<p class="row__total">$${item.total}</p>
//         `
//         tr.append(td_1)
//         tr.append(td_2)
//         tr.append(td_3)
//         tr.append(td_4)
//         fragment.append(tr)
//     }

//     table_body.append(fragment)
// }

// insertShopping()


// const removeItem = () => {
//     let bt_remove = document.getElementsByClassName('removeElement')
//     for(let bt of bt_remove){
//         bt.addEventListener('click', (e)=>{
//             let key_name = e.target.parentElement.parentElement.children[1].children[0].textContent
//             localStorage.removeItem(key_name)
//             e.target.parentElement.parentElement.remove()
//         })
//     }
// }

// removeItem()


// const calculateTotal = () => {
//     let row__input = document.getElementsByClassName('row__input')
//     for(let input of row__input){
//         input.addEventListener('input', (e)=>{
//             let key_name = e.target.parentElement.parentElement.children[1].children[0].textContent
//             item_actualizar = JSON.parse(localStorage.getItem(key_name))
//             item_actualizar.cantidad = e.target.value
//             item_actualizar.total = item_actualizar.cantidad*item_actualizar.item_price
//             localStorage.setItem(key_name, JSON.stringify(item_actualizar))
//         })
//     }
// }

// calculateTotal()

