Example project showing of ow to compile an run special compiler abilties like openmp offloading with clang.
Currently heavily under work. So most of the work ist still under development and NOT stable.


TODO:
=====
souper:
```bash
 --smtlib-abbreviation-mode=<value>                          - Choose abbreviation mode to use in SMT-LIBv2 files (default=let)
    =none                                                     -   Do not abbreviate
    =let                                                      -   Abbreviate with let
    =named                                                    -   Abbreviate with :named annotations
  --smtlib-display-constants=<value>                          - Sets how bitvector constants are written in generated SMT-LIBv2 files (default=dec)
    =bin                                                      -   Use binary form (e.g. #b00101101)
    =hex                                                      -   Use Hexadecimal form (e.g. #x2D)
    =dec                                                      -   Use decimal form (e.g. (_ bv45 8) )
  --smtlib-human-readable                                     - Enables generated SMT-LIBv2 files to be human readable (default=off)
  --solver-timeout=<int>                                      - Solver timeout in seconds (default=15)
  --souper-constant-synthesis-max-num-specializations=<uint>  - Maximum number of input specializations in constant synthesis (default=15).
  --souper-constant-synthesis-use-concrete-interpreter        - Use concrete interpreter in constant synthesis (default=false)
  --souper-dataflow-ai-phi                                    - Abstract interpret Phi instead of assuming first argument (default=false)
  --souper-dataflow-pruning                                   - Enable pruning based on dataflow analysis (default=false)
  --souper-dataflow-pruning-bb                                - Prune with bivalent-bits analysis (default=true)
  --souper-dataflow-pruning-cr                                - Prune with integer-ranges analysis (default=true)
  --souper-dataflow-pruning-fb                                - Prune with forced-bits analysis (default=true)
  --souper-dataflow-pruning-heavy                             - Enable all pruning techniques (default=false)
  --souper-dataflow-pruning-kb                                - Prune with known-bits analysis (default=true)
  --souper-dataflow-pruning-rb                                - Prune with required-bits analysis (default=true)
  --souper-debug-level=<uint>                                 - Control the verbose level of debug output (default=1). The larger the number is, the more fine-grained debug information will be printed.
  --souper-double-check                                       - Double check synthesis result with alive (default=false)
  --souper-enumerative-synthesis-cost-fudge=<uint>            - Generate guesses costing LHS + N (default=0)
  --souper-enumerative-synthesis-ignore-cost                  - Ignore cost of RHSs -- just generate them (default=false)
  --souper-enumerative-synthesis-max-instructions=<uint>      - Maximum number of instructions to synthesize (default=0).
  --souper-enumerative-synthesis-max-verification-load=<uint> - Maximum number of guesses verified at once (default=300).
  --souper-enumerative-synthesis-skip-solver                  - Skip refinement check after generating guesses (default=false)
  --souper-exploit-blockpcs                                   - Exploit block path conditions (default=false)
  --souper-external-cache                                     - Use external Redis-based cache (default=false)
  --souper-external-cache-unix                                - Talk to the cache using UNIX domain sockets (default=false)
  --souper-harvest-dataflow-facts                             - Perform data flow analysis (default=true)
  --souper-harvest-uses                                       - Harvest operands (default=false)
  --souper-internal-cache                                     - Cache solver results in memory (default=true)
  --souper-lsb-pruning                                        - Try to prune guesses by looking for a difference in LSB
  --souper-max-constant-synthesis-tries=<int>                 - Max number of constant synthesis tries. (default=30)
  --souper-max-lhs-cands=<uint>                               - Gather at most this many values from a LHS to use as synthesis inputs (default=10)
  --souper-max-lhs-size=<int>                                 - Max size of LHS (in bytes) to put in external cache (default=1024)
  --souper-no-infer                                           - Populate the external cache, but don't infer replacements (default=false)
  --souper-only-infer-i1                                      - Only infer integer constants with width 1 (default=false)
  --souper-only-infer-iN                                      - Only infer integer constants (default=false)
  --souper-redis-port=<uint>                                  - Redis server port (default=6379)
  --souper-shrink-consts                                      - Try to shrink constants (defaults=false)
  --souper-static-profile                                     - Static profiling of Souper optimizations (default=false)
  --souper-synthesis-comp-num=<int>                           - Maximum number of components (default=all)
  --souper-synthesis-const-with-cegis                         - Synthesis constants with CEGIS (default=false)
  --souper-synthesis-debug-level=<uint>                       - Synthesis debug level (default=0). The larger the number is, the more fine-grained debug information will be printed
  --souper-use-cegis                                          - Infer instructions (default=false)
  --speculative-counter-promotion-max-exiting=<uint>          - The max number of exiting blocks of a loop to allow  speculative counter promotion
  --speculative-counter-promotion-to-loop                     - When the option is false, if the target block is in a loop, the promotion will be disallowed unless the promoted counter  update can be further/iteratively promoted into an acyclic  region.
```
