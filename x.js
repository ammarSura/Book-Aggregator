const {PythonShell} = require('python-shell');

var results = false;
function getAllResults(keyword) {
    var c = 0;
    // const pyshell = new PythonShell('./Functs/searcher.py', {mode: "json"});
    const pyshell = new PythonShell('./Functs/searcher.py', {mode: "json"});

    let promise = new Promise (function(resolve, reject) {
    pyshell.send(keyword);

    pyshell.on('message', function (message) {
        
        // console.log('axe', message);
        // console.log(c);
        // c++;


        c = message;
        resolve(message);
        // c = c + message.
        // console.log('bv', message);
    
    });

    pyshell.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('finished');
    console.log('m', c.length, c);
    });

    setTimeout(() => {reject("Search timed out")} , 120000);

    })

    return promise;


}


async function getter() {
const x = await getAllResults("asimov");
return x;
// for (let i = 0; i <x.length; i++ ) {
//     console.log(String(i) + x[i]);
// }
}

// console.log(getter());
// console.log('as', x.length)
// getter()
// while(results) {
//     console.log('asa', results);
// }


module.exports = getAllResults;




