Copy Paste Data Grabber
==============

An example data plugin for Ship Data Science.
To use, simply add the following code to your model's .shipit.json.
The plugin just copies the data in text.txt to your data directory.
We use this plugin a lot for testing out functionality with small data sets.
You can fork the repo and change the contents of text.txt .

```
"data" : {
  "clone_url" : "THIS_REPO_URL",
  "args" : {
    "outPath" : ""
  }
}
```

FAQ
--------
Here is what happens to your data when you run a build:

 - A fresh virtual machine is spun up on AWS. This VM is only used for this build and deleted on termination.
 - Your model is cloned to the box using your Github oauth token.
 - This data plugin's environment is built using the Dockerfile.
 - This data plugin's docker container is started and the script writes your data to a mounted volume (a segregated file directory on your VM).
 - The docker container image is deleted and the data plugin is done.
 - Each monitoring plugin container you have selected is run sequentially and given access to the data directory.
 - The plugin results are sent to our server and the VM is terminated.
  


