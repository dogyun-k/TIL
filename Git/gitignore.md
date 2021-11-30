## gitignore

- 해당 파일에 기록된 파일, 디렉토리는 깃 관리 대상에서 제외한다.

## gitignore이 되지 않을 때

```sh
$ git rm -r --cached .
$ git add .
$ git commit -m "fixed untracked files"
```