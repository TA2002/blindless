//
//  ViewController.swift
//  Fireless
//
//  Created by Tarlan Askaruly on 17.09.2019.
//  Copyright © 2019 Tarlan Askaruly. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBAction func back(_ sender: UIButton) {
        self.dismiss(animated: true, completion: nil)
    }
    @IBOutlet weak var back: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }


}

