Idea:
----
Simple python script which enumerates given compiler flags and reruns different
benchmarks to find the optimal comninations of them

Examples:
----
```bash
python gcc_wrapper.py --path=test --target=example_c --regex="([+-]?([0-9]*[.])?[0-9]+)" --baseflags="-O3" --flags="--param=selsched-max-lookahead=1,-fschedule-fusion,-frename-registers,-fvect-cost-model=unlimited,-fsimd-cost-model=unlimited"
```

clang
---
pipeline:
```bash
clang -emit-llvm -c simple.c -o simple.bc
clang -S -emit-llvm simple.c -o simple.ll
```


Other useful commands:
show all possible passes
```bash
opt -print-passes
```

Usage of opt new pass manager
```bash
opt -enable-new-pm=1 -passes='no-op-function' simple.ll -S
```

get alot of inrofmations:
```bash
opt -stats -time-passes -enable-new-pm=1 -passes='no-op-function' simple.ll -S -o /dev/null
```

get alot of other information
```bash
opt -O1 foo.bc -debug-pass=Details -o /dev/null
opt -O1 foo.bc -debug-pass=Executions -o /dev/null
opt -O1 foo.bc -debug-pass=Structure -o /dev/null
```

Print the opt pipeline
```bash
opt -enable-new-pm=1 -O3 simple.ll -S -o /dev/null -print-changed=cdiff -print-after-all
```

```bash
opt -enable-new-pm=1 -adce -licm -simplifycfg -o /dev/null /dev/null -print-pipeline-passes
```
this shows all activated passed for a given optimisation flag. Note that 
`-print-pipeline-passes` is only available in newer clang packages.


Also there is a `-print-changed=dot-cfg` which outputs the change in the bitcode in a html file. 
https://clang.llvm.org/docs/UsersManual.html#opt-fdiagnostics-show-category


# Objdump

A small python script `objdump.py` is provided, which allows to control objdump 
to parse the assembly of certain functions



Rust:
----
Example on [godbolt](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:rust,selection:(endColumn:18,endLineNumber:4,positionColumn:18,positionLineNumber:4,selectionStartColumn:18,selectionStartLineNumber:4,startColumn:18,startLineNumber:4),source:'//+Type+your+code+here,+or+load+an+example.%0Apub+fn+square(num:+%26mut+%5Bu32%5D,+len:+usize)+-%3E+u32+%7B%0A++++let+mut+ret:+u32+%3D+0%3B%0A++++for+i+in+0..4+%7B%0A++++++++ret+%2B%3D+num%5Bi%5D%0A++++%7D%0A%0A++++return+ret%3B%0A%7D%0A%0A//+If+you+use+%60main()%60,+declare+it+as+%60pub%60+to+see+it+in+the+output:%0A//+pub+fn+main()+%7B+...+%7D%0A'),l:'5',n:'0',o:'Rust+source+%231',t:'0')),header:(),l:'4',m:25.205930807248766,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:nightly,filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',libraryCode:'0',trim:'1'),flagsViewOpen:'1',fontScale:14,fontUsePx:'0',j:1,lang:rust,libs:!(),options:'-Z+unstable-options++-Z+emit-stack-sizes+-Z+mir-opt-level%3D4++-C+opt-level%3D3+-Ctarget-cpu%3Dnative',selection:(endColumn:1,endLineNumber:1,positionColumn:1,positionLineNumber:1,selectionStartColumn:1,selectionStartLineNumber:1,startColumn:1,startLineNumber:1),source:1,tree:'1'),l:'5',n:'0',o:'rustc+nightly+(Rust,+Editor+%231,+Compiler+%231)',t:'0')),k:100,l:'4',m:49.79406919275123,n:'0',o:'',s:1,t:'0'),(g:!((h:output,i:(compilerName:'rustc+1.63.0',editorid:1,fontScale:14,fontUsePx:'0',j:1,wrap:'1'),l:'5',n:'0',o:'Output+of+rustc+nightly+(Compiler+%231)',t:'0')),header:(),l:'4',m:25,n:'0',o:'',s:0,t:'0')),l:'3',n:'0',o:'',t:'0')),version:4)

useful links:
	- [first](https://doc.rust-lang.org/beta/unstable-book/compiler-flags/self-profile.html)
	- [second](https://github.com/rust-lang/measureme)
	- [third](https://lazy.codes/posts/awesome-unstable-rust-features/)


# TODO
Extend to clang (--help-hidden)
