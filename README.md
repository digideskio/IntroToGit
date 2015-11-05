# IntroToGit
[![Build Status](https://travis-ci.org/RazoftOSS/Arbiter.svg?branch=feature%2Fswiss-pairing-dutch)](https://github.com/redbrick/IntroToGit)

# Workshop Help

- First, fork the repo. See that button that says fork? Press that.

- Okay, so now you have your very own git repo! How can you get that repo 
 on your account? Well you've got to **`clone`** the repo.

 So: go to your new repo.
 
 There should be a url that looks like this: 

     https://github.com/$username/IntroToGit.git
  
 On your terminal, run a `git clone` command, like so:

 ```
 git clone [url goes here]
 ```

 You'll be prompted for your password, but don't worry, it's HTTPS!

- Git will download the files and place them in a new directory, called 
`IntroToGit`

- It's good practice to have a separate branch for each new feature, so create one now.

- On that branch, make your changes. Add a new file in `names/` with your name.

- Stage your changes and commit them.

- Now push them up to your fork.

- Once you've done that, click the button that says "Compare and pull request",
and create a pull request to add your changes to the Redbrick repo.

# Workshop Stretch Goals #

If you've managed to do all that, try and figure out why our tests are failing and file a
Pull Request to fix them. `git bisect` might help you find out when it failed.
