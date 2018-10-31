# How to release

This is documenting the release process.


## Git flow & CHANGELOG.md

Make sure the CHANGELOG.md is up to date and follows the http://keepachangelog.com guidelines.
Start the release with git flow:
```
git flow release start YYYYMMDD
```
Now update the [CHANGELOG.md](/CHANGELOG.md) `[Unreleased]` section to match the new release version.
Also update the `version` string in the [setup.py](/setup.py) file. Then commit and finish release.
```
git commit -a -m "YYYYMMDD"
git flow release finish
```
Push everything, make sure tags are also pushed:
```
git push
git push origin master:master
git push --tags
```

## GitHub

Got to GitHub [Release/Tags](https://github.com/AndreMiras/pyetheroll/tags), click "Add release notes" for the tag just created.
Add the tag name in the "Release title" field and the relevant CHANGELOG.md section in the "Describe this release" textarea field.
Finally, attach the generated APK release file and click "Publish release".
