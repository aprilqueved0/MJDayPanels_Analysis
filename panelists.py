import json

# Create a Python dictionary
data = {
    "2019": {
        "spring": {
            "panelists": [
                "Sean Mussenden", "Sandy Banisky", "Ira Chinoy", 
                "Angela Wong (alum)", "Kevin Blackistone", 
                "Karen Denny", "Christine Harvey", "Alexander Pyles (alum)"
            ]
        },
        "fall": {
            "panelists": ["Kevin Blackistone", "Alison Burns", "Adam Marton", "Emily Yahr (Alum)", "Adrianne Flynn", "Kathy Best", "Sandy Banisky", "Alex Mann (Alum)", "Adam Marton", "DeNeen Brown", "Adrianne Flynn", "John O'Connor (Alum)", "Kevin Blackistone", "Alison Burns", "Bethany Swain", "Monica McNutt (Alum)", "Dana Priest", "Deb Nelson", "Krishnan Vasudevan", "Brooks Dubose (Alum)", "Tom Bettag", "Mel Coffee", "Alison Burns", "Gillian Morley (Alum)", "Kevin Blackistone", "Chris Harvey", "Marty Kaiser", "Rachel Pacella (Alum)", "Sandy Banisky", "Adrianne Flynn", "Sean Mussenden", "Julia Karron (Alum)", "Sean Mussenden", "Adam Marton", "Dana Priest", "Naema Ahmed (Alum)", "Sandy Banisky", "Adrianne Flynn", "Sean Mussenden", "George Gerbo (Alum)"
            ]
        }
    },
    "2020": {
        "spring": {
            "panelists": ["Adrianne Flynn", "Kevin Blackistone", "Bethany Swain", "Jamal Francis (alum)", "Adam Marton", "Krishnan Vasudevan", "Chris Harvey", "Lindsay Huth (alum)", "Clarence Williams", "Alison Burns", "Tim Jacobsen", "Lindsay Simpson (alum)", "Chris Harvey", "Alison Burns", "Tom Bettag", "Regina Ham (alum)", "Sandy Banisky", "Adrianne Flynn", "Kevin Klose", "George Gerbo (alum)", "Adam Marton", "Sean Mussenden", "Deb Nelson", "Lindsay Huth (alum)", "Chris Harvey", "Jim Carroll", "Sandy Banisky", "Idrees Ali (alum)", "Sean Mussenden", "Adam Marton", "Dana Priest", "Hannah Gaskill (alum)", "Adrianne Flynn", "Deb Nelson", "Sean Mussenden", "Julie Depenbrock (alum)"]
        },
        "fall": {
            "panelists": ["Kevin Blackistone", "Mel Coffee", "Josh Davidsburg", "Julia Karron (alum)", "Tom Bettag", "Sandy Banisky", "Sean Mussenden", "Brooke Howell (alum)", "Jim Carroll", "Deb Nelson", "Kathy Best", "Joe Yasharoff (alum)", "Josh Davidsburg", "Chris Harvey", "Adrianne Flynn", "Britt Waters (alum)", "Dana Priest", "Deb Nelson", "Kathy Best", "Danielle Ohl (alum)", "Kevin Blackistone", "Adam Marton", "Jim Carroll", "Monica McNutt (alum)", "Chris Harvey", "Adrianne Flynn", "Sandy Banisky", "Emily Yahr (alum)", "Chris Harvey", "Sandy Banisky", "Alex Pyles", "Brooke Auxier (Alum)", "Adrianne Flynn", "Adam Marton", "Sean Mussenden", "Lindsay Huth (alum)", "Marty Kaiser", "Connie Ford", "Deb Nelson", "Chris Matthews (alum)", "Tom Bettag", "Mel Coffee", "Josh Davidsburg", "Jasmine Whittington (alum)", "Sean Mussenden", "Deb Nelson", "Bob Little", "Kelley Benham French (alum)", "Mel Coffee", "Josh Davidsburg", "Bethany Swain", "Carly Haynes (alum)"]
        }
    },
    "2021": {
        "spring": {
            "panelists": ["Sandy Banisky", "Alex Pyles", "Sean Mussenden", "Jaclyn Borowski (alum)", "Christine Harvey", "Kathy Best", "Jim Carroll", "Emily Yahr (alum)", "Adrianne Flynn", "Karen Denny", "Edward Alwood", "Alex Mann (alum)", "Mark Feldstein", "Deborah Nelson", "Tom Bettag", "Arya Hodjat (alum)", "Mark Hyman", "Mark Selig", "George Solomon", "Kate Yanchulis (alum)", "Christine Harvey", "Sean Mussenden", "Bob Little", "Emily Yahr (alum)", "Bob Little", "Adrianne Flynn", "Deneen Brown", "Anika Reed (alum)", "Mel Coffee", "Josh Davidsburg", "Sandy Banisky", "Karen Castillo (alum)", "Alexander Pyles", "Constance Ford", "Chris Harvey", "Hannah Gaskill (alum)", "Deb Nelson", "Chris Harvey", "Jim Carroll", "Elliott Davis (alum)", "Robert Ruby", "Alex Pyles", "Jim Carroll", "Laura Thornton (alum)", "Chris Harvey", "Sandy Banisky", "Alex Pyles", "Anika Reed (alum)", "Karen Denny", "Bob Little", "Adrianne Flynn", "Nora Eckert (alum)", "Mel Coffee", "Bethany Swain", "Josh Davidsburg", "Carly Haynes (alum)", "Alex Pyles", "Kathy Best", "Adrianne Flynn", "Monica Norton (alum)", "Kate Yanchulis", "Sean Mussenden", "Alex Pyles", "Daniel Oyefusi (alum)", "Chris Harvey", "Adrianne Flynn", "Robert Ruby"]
        },
        "fall": {
            "panelists": ["Adam Marton", "Tom Davidson", "DeNeen Brown", "Chris Cioffi (alum)", "Adrianne Flynn", "Dana Priest", "James Carroll", "Alicia McElhaney (alum)", "James Carroll", "Mauro Whiteman", "Chris Harvey", "Maria Douglas Reeve (alum)", "Adrianne Flynn", "Sandy Banisky", "Tom Bettag", "Alex Pyles (alum)", "Rob Little", "Sean Mussenden", "Deb Nelson", "Julia Karron (alum)", "Tom Bettag", "Mauro Whiteman", "Alison Burns", "Rachel Hirschheimer (alum)", "DeNeen Brown", "Sandy Banisky", "Dana Priest", "Regina Ham (alum)", "Sean Mussenden", "Adam Marton", "Josh Davidsburg", "Alex Pyles (alum)"]
        }
    },
    "2022": {
        "spring": {
            "panelists": ["Derek Willis", "Sean Mussenden", "Adam Marton", "Ryan Little (alum)", "Bethany Swain", "Josh Davidsburg", "Dana Priest", "Cheryl Costello (alum)", "Mark Hyman", "Kevin Blackistone", "Jim Carroll", "Jesse Yomtov (alum)", "Deb Nelson", "Kathy Best", "Adam Marton", "Nora Eckert (alum)", "Jim Carroll", "Kevin Blackistone", "Nathaniel Stevens", "Allison Williams (alum)", "Bethany Swain", "Josh Davidsburg", "Chris Harvey", "Cheryl Costello (alum)", "Derek Willis", "Sean Mussenden", "Deb Nelson", "Ryan Little (alum)", "Deborah Nelson", "Dana Priest", "DeNeen Brown", "Arelis Hernandez (alum)", "Deb Nelson", "Derek Willis", "Adam Marton", "Ivan Penn (alum)", "Derek Willis", "Sean Mussenden", "Adam Marton", "Naema Ahmed (alum)", "Derek Willis", "Alex Pyles", "Joe Yasharoff", "Christy Winters Scott (alum)"]
        },
        "fall": {
            "panelists": ["Josh Davidsburg", "Mel Coffee", "Bethany Swain", "Alison Burns (alum)", "Adam Marton", "Kathy Best", "Tom Rosenstiel", "Molly Work (alum)", "Mel Coffee", "Alison Burns", "Joe Yasharoff", "Josh Davidsburg (alum)", "Alex Pyles", "Derek Willis", "Tom Rosenstiel", "Ryan Little (alum)", "Mel Coffee", "Alison Burns", "Josh Davidsburg", "Jason Newton (alum)", "Rob Wells", "Adam Marton", "Dana Priest", "Brenda Wintrode (alum)", "Mel Coffee", "Nathan Stevens", "Bethany Swain", "Josh Davidsburg (alum)", "Jim Carroll", "Tom Rosenstiel", "Tom Davidson", "Steven Overly (alum)", "Mark Hyman", "Derek Willis", "Sandy Banisky", "Timothy Gardner (alum)", "Bob Little", "Kathy Best", "Jim Carroll", "Julie Depenbrock (alum)", "Derek Willis", "Sean Mussenden", "Adam Marton", "Sandy Banisky", "Dana Priest", "Jim Carroll", "Arelis Hernandez (alum)", "Mel Coffee", "Joe Yasharroff", "Nathan Stevens", "Josh Davidsburg (alum)", "Dana Priest", "Jim Carroll", "Constance Ford", "Idrees Ali (alum)", "Derek Willis", "Adam Marton", "Kevin Blackistone", "Lee Zeidman (alum)"]
        }
    },
    "2023": {
        "spring": {
            "panelists": ["Derek Willis", "Sean Mussenden", "Tom Rosenstiel", "Jackie Incollingo (alum)", "Kevin Blackistone", "Derek Willis", "Mark Hyman", "Mark Selig (alum)", "Adam Marton", "Sean Mussenden", "Derek Willis", "Aadit Tambe (alum)", "Mel Coffee", "Alison Burns", "Josh Davidsburg", "Max Marcilla (alum)", "Bob Little", "Dana Priest", "Jim Carroll", "Allison Michaels (alum)", "Adam Marton", "Sandy Banisky", "Jim Carroll", "Aadit Tambe (alum)", "Adam Marton", "Derek Willis", "Alex Pyles", "Aadit Tambe (alum)", "Derek Willis", "Kevin Blackistone", "Chris Harvey", "Mark Selig (alum)", "Alex Pyles", "Thomas Rosenstiel", "Kathy Best", "Jummy Owookade (alum)", "Constance Ford", "Thomas Rosenstiel", "Derek Willis", "Kathy Best", "Nick McMillan (alum)", "Alex Pyles", "DeNeen Brown", "Tom Rosenstiel", "Tayler Adigun (alum)"]
        },
        "fall": {
            "panelists": ["Kevin Blackistone", "Josh Davidsburg", "Allison Burns", "Cheryl Connor (alum)", "Alex Pyles", "Mel Coffee", "Josh Davidsburg", "Ya-Marie Sesay (alum)", "Josh Davidsburg", "Kevin Blackistone", "Krishnan Vasudevan", "Alex Flum (alum)", "Kaitlyn Wilson", "Mark Hyman", "Kevin Blackistone", "Reese Levin (alum)", "Rob Wells", "Adam Marton", "Kathy Best", "Brenda Wintrode (alum)", "Josh Davidsburg", "Mel Coffee", "Christoph Mergerson", "Brendan Hartlove (alum)", "Josh Davidsburg", "Krishnan Vasudevan", "Alana Delfino Kopania", "Mark Hyman", "Alex Glass (alum)", "Alex Pyles", "Jim Carroll", "Kathy Best", "Betty Chu (alum)", "Kathy Best", "Alex Pyles", "Dana Priest", "Jackie Incollingo (alum)", "Derek Willis", "Jim Carroll", "Tom Rosenstiel", "Maite Fernandez Simon (alum)", "Mark Hyman", "Derek Willis", "Tom Rosenstiel", "Jackie Incollingo (alum)", "Kathy Best", "Derek Willis", "Rachel Marconi (alum)"]
        }
    },
    "2024": {
        "spring": {
            "panelists": ["Kathy Best", "Tom Rosenstiel", "Jim Carroll", "Emmett Gartner (alum)", "Josh Davidsburg", "Kevin Blackistone", "Alanna Delfino", "Alex Glass (alum)", "Chris Harvey", "Stacey Decker", "Derek Willis", "Eva Sanchez (alum)", "Dana Priest", "Kathy Best", "Christoph Mergerson", "Kara Newhouse (alum)", "Dana Priest", "Jim Carroll", "Derek Willis", "Kara Newhouse (alum)", "Dana Priest", "Kathy Best", "Derek Willis", "Idrees Ali (alum)", "Mark Hyman", "Sean Mussenden", "Christi Parsons", "Greg Schimmel (alum)", "Kathy Best", "Christi Parsons", "Deb Nelson", "Brenda Wintrode (alum)"]
        },
        "fall": {
            "panelists": ["Bob Little", "Steve Drummond", "Deb Nelson", "Chris Frates (alum)", "Christi Parsons", "Alanna Delfino", "Kevin Blackistone", "Rob Carlin (alum)", "Mel Coffee", "Alison Burns", "Alanna Delfino", "Ya-Marie Sesay (alum)", "Mel Coffee", "Alison Burns", "Cindy Wright", "Nicole Curtis (alum)", "Christoph Mergerson", "Dana Priest", "Derek Willis", "Karl Hille (alum)", "Deneen Brown", "Tom Rosenstiel", "Adam Marton", "Jon Meltzer (alum)", "Kevin Blackistone", "Rob Wells", "Jim Carroll", "Jackie Incollingo (alum)", "Adam Martin", "Mark Hyman", "Chris Harvey", "Sapna Bansil (alum)", "Christi Parsons", "Tim Jacobsen", "DeNeen Brown", "Joy Saha (alum)"]
        }
    },
    "2025": {
        "spring": {
            "panelists": ["Derek Willis", "Kathy Best", "Sean Mussenden", "Adam Marton", "Rachel Marconi (alum)", "Adam Marton", "Derek Willis", "Kathy Best", "Chris Harvey", "Greg Morton (alum)", "Nathan Stevens", "Josh Davidsburg", "Alanna Kopania", "Eugene Obah (alum)", "Adam Marton", "Rick Martin (alum)", "Alanna Kopania", "Josh Davisburg", "Keir Johnson (alum)", "Sean Mussenden", "Ryan Little", "Christi Parsons", "Sapna Bansil (alum)", "Mark Hyman", "Kevin Blackistone", "Stacey Decker", "Megan Sayles (alum)", "Chris Harvey", "Kathy Best", "Adam Marton", "Sapna Bansil (alum)", "Christi Parsons", "Christoph Mergerson", "Derek Willis", "Brenda Wintrode (alum)", "Rob Wells", "Kathy Best", "Derek Willis", "Ryan Little (alum)", "Mel Coffee", "Kevin Blackistone", "Joe Yasharoff", "Monica McNutt (alum)", "Tom Rosenstiel", "Bob Little", "Stev Drummond", "Julie Depenbrock (alum)", "Jim Carroll", "DeNeen Brown", "Dana Priest", "Nathan Stevens", "Jamal Francis (alum)"]
        }
    }
}

# Write to a JSON file
with open("panel_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)  # `indent` makes it pretty