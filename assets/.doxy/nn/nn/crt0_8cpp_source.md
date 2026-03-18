

# File crt0.cpp

[**File List**](files.md) **>** [**crt0**](dir_24f5be450dfa709e190b6f431391bee8.md) **>** [**MPCore**](dir_5ef632110aebbd6ea53d3bca60abe996.md) **>** [**crt0.cpp**](crt0_8cpp.md)

[Go to the documentation of this file](crt0_8cpp.md)


```C++
#include <nn/svc/svc_Api.h>
#include <rt_locale.h>
#include <rt_sys.h>

extern "C" void nninitRegion();
extern "C" void nninitLocale();
extern "C" void nninitSystem();
extern "C" void nninitStartUp();

extern "C" __weak void   __cpp_initialize_aeabi_();
extern "C" unsigned int* __rt_locale( void );

extern "C" void nninitCallStaticInitializers();
extern "C" void nninitSetup();
extern "C" void nnMain();

extern "C" unsigned char Image$$ZI$$ZI$$Base[];
extern "C" unsigned char Image$$ZI$$ZI$$Limit[];

extern "C" __asm void __ctr_start()
{
        // clang-format off
    bl __cpp(nninitRegion)
    bl __cpp(nninitLocale)
    bl __cpp(nninitSystem)
    bl __cpp(nninitStartUp)
    bl __cpp(__cpp_initialize_aeabi_) // this is being nopped
    bl __cpp(nninitCallStaticInitializers)
    bl __cpp(nninitSetup)
    bl __cpp(nnMain)
    b __cpp(nn::svc::ExitProcess)
        // clang-format on
}

extern "C" __asm void nninitRegion()
{
        // clang-format off
    ldr r0, =__cpp(Image$$ZI$$ZI$$Base)
    ldr r1, =__cpp(Image$$ZI$$ZI$$Limit)
    mov r2, #0
run
    cmp r0, r1
    strcc r2, [r0], #4
    bcc run
    bx lr
        // clang-format on
}

extern "C" void nninitLocale()
{
        unsigned int* rt = __rt_locale();
        *( rt + 1 )      = (unsigned int)_get_lc_ctype( 0, 0 ) + 1;
        *( rt + 3 )      = (unsigned int)_get_lc_numeric( 0, 0 );
}
// clang-format on
```


