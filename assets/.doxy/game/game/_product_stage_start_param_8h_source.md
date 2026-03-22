

# File ProductStageStartParam.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Sequence**](dir_add35431d27bbd5f0559725cdc453615.md) **>** [**ProductStageStartParam.h**](_product_stage_start_param_8h.md)

[Go to the documentation of this file](_product_stage_start_param_8h.md)


```C++
#pragma once

class StageStartParamBase
{
public:
        virtual const char* getStageDataName();
        virtual int         getScenario();
        virtual void*       getUnk2();
        virtual void*       getUnk3();
        virtual void*       getUnk4();

private:
        virtual void gap();
        virtual void gap2();

public:
        virtual int getUnk5();
};

class ProductStageStartParam : public StageStartParamBase
{
private:
        void* unk[ 2 ];
        int   mScenario;

public:
        virtual const char* getStageDataName();

        virtual int getScenario()
        {
                return mScenario;
        }

        virtual void* getUnk2();
        virtual void* getUnk3();
        virtual void* getUnk4();

        const char* getDemoStageName() const;
};
```


