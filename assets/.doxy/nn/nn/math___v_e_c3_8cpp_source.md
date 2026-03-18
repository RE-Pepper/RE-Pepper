

# File math\_VEC3.cpp

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**sources**](dir_6ad72fc0abbc32b2f59992fddd21f3c1.md) **>** [**math**](dir_79e41db79b7fa8bfabe0e320694d691f.md) **>** [**math\_VEC3.cpp**](math___v_e_c3_8cpp.md)

[Go to the documentation of this file](math___v_e_c3_8cpp.md)


```C++
#include <nn/math/math_VEC3.h>

namespace nn {
namespace math {
    namespace ARMv6 {

        // clang-format off

    __asm void __attribute__((section("i._ZN2nn4math5ARMv610VEC3SubAsmEPNS0_4VEC3EPKS2_S5_"))) VEC3SubAsm(VEC3* out, const VEC3* v1, const VEC3* v2)
    {
        vldmia r1, {s0, s1, s2}
        vldmia r2, {s3, s4, s5}
        vsub.f32 s6, s0, s3
        vsub.f32 s7, s1, s4
        vsub.f32 s8, s2, s5
        vstmia r0, {s6, s7, s8}
        bx lr
    }

    __asm void __attribute__((section("i._ZN2nn4math5ARMv610VEC3MulAsmEPNS0_4VEC3EPKS2_f"))) VEC3MulAsm(VEC3* out, const VEC3* v1, float f)
    {
        vldmia r1, {s1, s2, s3}
        vmul.f32 s4, s1, s0
        vmul.f32 s5, s2, s0
        vmul.f32 s6, s3, s0
        vstmia r0, {s4, s5, s6}
        bx lr
    }

        // clang-format on

    } // namespace ARMv6
} // namespace math
} // namespace nn
```


