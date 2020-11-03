import UIKit

//public var array2D: [[[String]]] = [[["Keruen", "1.jpg"], ["Mega Silkway", "2.jpg"]], [["Khan Shatyr", "3.jpg"], ["Saryarka", "4.jpg"]]]
public var tcname: [String] = ["Keruen", "Mega Silkway", "Khan Shatyr", "Saryarka"]
public var tcimage: [String] =  ["1.jpg", "2.png", "3.png", "4.jpg"]


class TableViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    public func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return tcname.count
    }
    
    public func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as! TableViewCell
        cell.name.text = tcname[indexPath.row]
        cell.photo.image = UIImage(named: tcimage[indexPath.row])
        print("indexPath.row")
        return cell
    }
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    
}

