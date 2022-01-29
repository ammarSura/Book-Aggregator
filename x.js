const {PythonShell} = require('python-shell');


function getAllResults(keyword) {
    const pyshell = new PythonShell('./Functs/searcher.py', {mode: "json"});

    let promise = new Promise (function(resolve, reject) {
    pyshell.send(keyword);

    pyshell.on('message', function (message) {
        
        resolve(message);
    
    });

    pyshell.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('finished');
    });

    setTimeout(() => {reject("Search timed out")} , 120000);

    })

    return promise;


}

// async function getter() {
//     await getAllResults("asimov").then( (result) => {
//         console.log('res', result);
//     }, (error) => {
//         console.log('err', error);
//     });

//     // console.log('answer', ans);
// }

// const x = getAllResults("asimov");

// // console.log('as', x)
// getter()


module.exports = getAllResults;




