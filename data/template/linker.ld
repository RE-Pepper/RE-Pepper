TEXT_SECTION //T
{
    STUP_ENTRY  +0
    {
///
    }
    INIT_ARRAY  +0 
    {
        * (.init_array)
    }
}

RO_SECTION //O
{
    RO  +0
    {
&&&
    }
    STATIC_INIT  +0 
    {
        * (.static_init)
    }
    ET +0
    {
        * (.ARM.exidx)
        * (.ARM.extab)
    }
}

RW_SECTION //W
{
    RW +0
    {
###
    }
    ZI +0
    {
???
    }
}

/* 0x04000000 in real game */
MODULE_INFO     (//T + (0x01000000 - 0x00100000))
{
    .module_id  (//T + (0x01000000 - 0x00100000))
    {
        * (.module_id)
    }
}

GARBAGE_SECTION +0
{
    REST_SECTION +0
    {
        * (+RO-CODE)
        * (+CONST)
        * (+RW-DATA)
        * (+ZI)
    }
}
