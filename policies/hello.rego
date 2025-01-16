package policies.play

default hello = false

hello {
    m := input.message
    m == "world"
}