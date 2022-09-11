if (window.fetch != undefined) console.log('FETCH OK')
else console.log('FETCH NOT WORKS!')

fetch('')
.then(res=>res.ok ? Promise.resolve(res) : Promise.reject(res))
.then(res=>res.json ())
.then(res=>console.log(res))