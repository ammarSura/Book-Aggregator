const {PythonShell} = require('python-shell');

var results = false;
function getAllResults(keyword) {
    
    const pyshell = new PythonShell('./Functs/searcher.py', {mode: "json"});

    var promise = new Promise (function(resolve, reject) {

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

        });

    return promise;


}


async function getter() {
const x = await getAllResults("asimov");
return x;

}

module.exports = getAllResults;




