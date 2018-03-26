// chain: get price -> convert -> transfer

function banking() {
    $.getJSON("/price/ABC/").then(function(res) {
        console.log("got price", res.price);
        return $.getJSON(`/convert?usd=${res.price}`)
    }).then(function(res) {
        console.log("in rithmcoin", res.rithmcoin);
        return $.getJSON(`/transfer?amt=${res.rithmcoin}`)
    }).then(function (res) {
        console.log(res.msg);
    })
}


// want all answers, but in any order

function weather() {
    let w1 = $.getJSON("/weather/11223/");
    let w2 = $.getJSON("/weather/21122/");
    let w3 = $.getJSON("/weather/94114/");
    Promise.all([w1, w2, w3]).then(function (res) {
        console.log(res);
    });
}


// we'll ask all 3 but we only care about first response

function anyJoke() {
    let j1 = $.getJSON("/joke-1");
    let j2 = $.getJSON("/joke-2");
    let j3 = $.getJSON("/joke-3");
    Promise.race([j1, j2, j3]).then(function (res) {
        console.log(res);
    });
}

