<h2><a id="user-content-stack" class="anchor" aria-hidden="true" href="#stack"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Stack</h2>
<p>Fifth is a new stack-based language. A stack is a data structure which can only have elements added to the top.
Fifth stores a stack of integers and supports commands to manipulate that stack.
Operations always apply to the top of the stack.</p>
<p>Fifth supports the following arithmetic operators:</p>
<pre><code>+ - * /
</code></pre>
<p>Each of these applies the operator to the two values on the top of the stack and pushes the
result to the top of the stack. If division results in a non-integer, round down.</p>
<p>Fifth also supports the following commands:</p>
<ul>
<li><code>PUSH x</code> - push x onto the top of the stack, where x is a valid integer</li>
<li><code>POP</code> - remove the top element of the stack</li>
<li><code>SWAP</code> - swap the top two elements of the stack</li>
<li><code>DUP</code> - duplicate the top element of the stack</li>
</ul>
<p>Write a python program which works as a fifth interpreter. Each line of input to the program should
represent a single fifth command. Output the result of each command to the terminal. Handle errors sensibly.</p>
<p>Example:</p>
<pre><code>stack is []
PUSH 3
stack is [3]
PUSH 11
stack is [3, 11]
+
stack is [14]
DUP
stack is [14, 14]
PUSH 2
stack is [14, 14, 2]
*
stack is [14, 28]
SWAP
stack is [28, 14]
/
stack is [2]
+
ERROR
</code></pre>
</article>
      </div>
  </div>
