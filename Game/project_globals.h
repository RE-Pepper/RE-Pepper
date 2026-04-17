#include <nn/types.h>

#ifndef RP_SHUTUP
#define RP_SHUTUP \
        _Pragma("diag_suppress 177,550,940")
#endif

// Assertion
#ifndef static_assert
#define static_assert(COND, MSG) typedef int __static_assert_failed[(COND) ? 1 : -1]
#endif
#define static_assert_(COND) static_assert(COND, #COND)

#ifdef __arm__ // Used by compiler

#define force_section(Section) __attribute__((section(Section)))

#define force_func_section(Symbol) force_section("i." #Symbol)

#define var(Namespace, Name, Type) static Type force_section(".sdata_" #Namespace "::" #Name) Name
#define varc(Namespace, Class, Name, Type) Type force_section(".sdata_" #Namespace "::" #Name) Class::Name
#define varg(Name, Type) static Type force_section(".sdata_" #Name) Name
#define varcg(Class, Name, Type) Type force_section(".sdata_" #Name) Class::Name

#define asm_ext(Name, Sect) __asm force_section(Sect) Name
#define asm(Name) asm_ext(Name, "i." #Name)

#else // Used by editor

#define NN_SWITCH_DISABLE_ASSERT_WARNING_FOR_SDK 1
#define NN_SWITCH_DISABLE_DEBUG_PRINTING_FOR_SDK 1

// Force a section name
#define force_section(Section)

#define force_func_section(Symbol)

// Force a section for static namespaced variables
// Example: var(nn::fs, s_Initialized, bool) = False // == bool s_Initialized;
//     -> nn::fs::s_Initialized in symbol map
// Example: var(nn::fs, s_Array, u32)[64] = ...
//     -> nn::fs::s_Array in symbol map
#define var(Namespace, Name, Type) Type Name
// the class variant
// Example: varc(al, ActorActionKeeper, sGravity, f32) = 0.f; // == f32 ActorActionKeeper::sGravity = 0.f;
#define varc(Namespace, Class, Name, Type) Type Class::Name

// Force a section for static global variables
// Example: varcg(s_Something, u32) = 3 // == u32 s_Something = 3;
//     -> s_Something in symbol map
#define varg(Name, Type) Type Name
// the class variant
// Example: varcg(CoolEnemy, f32) = 0.f; // == f32 CoolEnemy
#define varcg(Name, Class, Type) Type Class::Name

// Force a section for assembly functions, with custom namespace (for some nn stuff)
// Example: asm_ext(SendSyncRequest, ".nn.svc.SendSyncRequest") (Handle handle) { ... }
//     -> WIP
#define asm_ext(Name, Sect) Name

// Force a section for assembly functions
// Example: asm(nninitRegion) (void) { ... }
#define asm(Name) Name

#define __weak
#define __clrex()
#endif
