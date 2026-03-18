

# File math\_VEC3.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**math**](dir_f04f036a24ab4e9b968e47fb2e928fcd.md) **>** [**math\_VEC3.h**](math___v_e_c3_8h.md)

[Go to the documentation of this file](math___v_e_c3_8h.md)


```C++
#pragma once

namespace nn {
namespace math {

    struct VEC3 {
        float x;
        float y;
        float z;
    };

    namespace ARMv6 {

        void VEC3AddAsm(VEC3* out, const VEC3* v1, const VEC3* v2);
        void VEC3SubAsm(VEC3* out, const VEC3* v1, const VEC3* v2);
        void VEC3MulAsm(VEC3* out, const VEC3* v1, const VEC3* v2);
        void VEC3DivAsm(VEC3* out, const VEC3* v1, const VEC3* v2);

        void VEC3AddAsm(VEC3* out, const VEC3* v1, float f);
        void VEC3SubAsm(VEC3* out, const VEC3* v1, float f);
        void VEC3MulAsm(VEC3* out, const VEC3* v1, float f);
        void VEC3DivAsm(VEC3* out, const VEC3* v1, float f);

    } // namespace ARMv6

} // namespace math
} // namespace nn
```


