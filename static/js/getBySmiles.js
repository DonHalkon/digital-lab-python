function findBySmiles() {
    let myButton = document.getElementById("find-by-smiles-button");
    myButton.disabled = true;
    try {
        let smiles = jsmeApplet.smiles();
        if ('' !== smiles) {
            // console.log(smiles)
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var result = JSON.parse(this.responseText).PropertyTable.Properties[0];
                    // console.log(xmlHttp.responseText)
                    if (Object.keys(result).length > 2) {
                        document.getElementById("id_iupacName").value = result.IUPACName;
                        document.getElementById("id_cid").value = result.CID;
                        document.getElementById("id_molecularFormula").value = result.MolecularFormula;
                    } else {
                        alert("Compound was not found!")
                    }

                }
            };
            xmlHttp.open("GET", "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/" + encodeURI(smiles) + "/property/IUPACName,MolecularFormula,MolecularWeight/JSON", true); // false for synchronous request
            xmlHttp.send(null);
        }
    } finally {
        myButton.disabled = false;
    }
}