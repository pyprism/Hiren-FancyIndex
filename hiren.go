package main

import (
	"fmt"
	"io/ioutil"
	"log"
	//	"os"
)

func main() {
	file, e := ioutil.ReadFile("./config.json")
	if e != nil {
		fmt.Printf("File error: %v\n", e)
		fmt.Println(e.Error())
		//log.Fatal(e)
		//os.Exit(1)
	}
	//var jsonobject jsontype
	fmt.Printf("%s\n", string(file))
	files, err := ioutil.ReadDir("/home/prism/")
	if err != nil {
		log.Fatal(err)
	}
	for _, f := range files {
		fmt.Println(f.Name())
		fmt.Println(f.IsDir())
		fmt.Println(f.Size())
	}
}

// package main
//
// import (
// 	"fmt"
// 	"path/filepath"
// )
//
// func main() {
// 	files, _ := filepath.Glob("*")
// 	fmt.Println(files) // contains a list of all files in the current directory
// }
