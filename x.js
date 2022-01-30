const {PythonShell} = require('python-shell');

var results = false;
function getAllResults(keyword) {
    // const pyshell = new PythonShell('./Functs/searcher.py', {mode: "json"});
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

async function getter() {
    await getAllResults("asimov").then( (result) => {
        console.log('res', result[0]);
        results = result;
    }, (error) => {
        console.log('err', error);
        results = error;
    });

    // console.log('answer', ans);
}

// const x = getAllResults("asimov");

// // console.log('as', x)
// getter()
// while(results) {
//     console.log('asa', results);
// }


module.exports = getAllResults;




