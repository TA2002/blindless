//
//  NewViewController.swift
//  Fireless
//
//  Created by Tarlan Askaruly on 09.03.2020.
//  Copyright © 2020 Tarlan Askaruly. All rights reserved.
//

import Foundation
import UIKit

//public var array2D: [[[String]]] = [[["Keruen", "1.jpg"], ["Mega Silkway", "2.jpg"]], [["Khan Shatyr", "3.jpg"], ["Saryarka", "4.jpg"]]]
//public var tcname2: [String] = ["Keruen", "Mega Silkway", "Khan Shatyr", "Saryarka"]
//public var tcimage2: [String] =  ["1.jpg", "2.png", "3.png", "4.jpg"]

public var tcname2: [String] = ["Keruen", "Khan Shatyr"]
public var tcimage2: [String] =  ["1.jpg", "3.png"]

class NewViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    public func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return tcname2.count
    }
    
    public func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell2 = tableView.dequeueReusableCell(withIdentifier: "newcell", for: indexPath) as! NewTableViewCell
        cell2.namee.text = tcname2[indexPath.row]
        cell2.picta.image = UIImage(named: tcimage2[indexPath.row])
        print("\(indexPath.row)")
        return cell2
    }
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        if(searchBar.text == nil || searchBar.text == ""){
            isSearching = false
            view.endEditing(true)
            myTableView.reloadData()
        }
        else{
            isSearching = true
            FilteredData = [[]]
            for number in 0..<(array2D.count){
                if((array2D[number].name as NSString).contains(searchBar.text!)){
                    FilteredData.append(array2D[number])
                }
            }
            myTableView.reloadData()
        }
    }
    
    
}

