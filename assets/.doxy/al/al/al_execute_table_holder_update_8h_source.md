

# File alExecuteTableHolderUpdate.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Execute**](dir_b0627dbdf07c5051f864ccb41a35881f.md) **>** [**alExecuteTableHolderUpdate.h**](al_execute_table_holder_update_8h.md)

[Go to the documentation of this file](al_execute_table_holder_update_8h.md)


```C++
#pragma once

namespace al
{

class ExecuteOrder;
class FunctorBase;

class IUseExecutor;

class ExecuteTableHolderUpdate
{
        friend class ExecuteDirector;

private:
        int _0;
        int _4;
        int _8;
        int _C;
        int _10;
        int _14;
        int _18;
        int _1C;
        int _20;
        int _24;
        int _28;
        int _2C;
        int _30;
        int _34;
        int _38;
        int _3C;
        int _40;

public:
        void init( const ExecuteOrder* order, int );
        void createExecutorListTable();
        void tryRegisterUser( al::IUseExecutor* p, const char* name );
        void tryRegisterFunctor( const al::FunctorBase& base, const char* name );

public:
        ExecuteTableHolderUpdate();
};

} // namespace al
```


