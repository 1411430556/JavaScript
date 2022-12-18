// import * as m1 from "./hello.js";    静态加载

// 获取元素
const btn = document.getElementById('btn')
btn.onclick = function () {
  import('./hello.js').then(module => {
    // console.log(module)  返回一个promise对象
    module.hello()
  })
}