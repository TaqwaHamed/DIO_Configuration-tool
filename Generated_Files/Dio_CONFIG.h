/****************************************************************************************
*******************************   Author  : Taqwa Hamed    ******************************
*******************************   SWC     : Dio_Config.h   ******************************
*******************************   Version : Version 01     ******************************
****************************************************************************************/
#ifndef _DIO_CONFIG_H
#define _DIO_CONFIG_H


#include "std_types.h"
#include "Dio_INTERFACE.h"  

/****************************************************************************************
************** Don't Change The following MACROS *******************
****************************************************************************************/
#define  OUTPUT_HIGH     ((u8)0)
#define  INPUT_PULL_UP   ((u8)1)
#define  INPUT_HIGH_IMP  ((u8)2)
#define  OUTPUT_LOW      ((u8)3)


/****************************************************************************************
************** Don't Change The following MACROS   *******************
************** MicroController Pins Configurations *******************
****************************************************************************************/

#define NUM_OF_PINS     ((u8)10)

#define PIN0_CONFIG        ((u8)OUTPUT_HIGH)
#define PIN1_CONFIG        ((u8)OUTPUT_LOW)
#define PIN2_CONFIG        ((u8)OUTPUT_HIGH)
#define PIN3_CONFIG        ((u8)OUTPUT_LOW)
#define PIN4_CONFIG        ((u8)INPUT_PULL_UP)
#define PIN5_CONFIG        ((u8)INPUT_HIGH_IMP)
#define PIN6_CONFIG        ((u8)INPUT_PULL_UP)
#define PIN7_CONFIG        ((u8)INPUT_PULL_UP)
#define PIN20_CONFIG        ((u8)OUTPUT_HIGH)
#define PIN14_CONFIG        ((u8)INPUT_HIGH_IMP)


DIO_Pin_Configurations_ST DIO_PINS_arr[NUM_OF_PINS] = { 
                   {PIN0, PIN0_CONFIG},
                   {PIN1, PIN1_CONFIG},
                   {PIN2, PIN2_CONFIG},
                   {PIN3, PIN3_CONFIG},
                   {PIN4, PIN4_CONFIG},
                   {PIN5, PIN5_CONFIG},
                   {PIN6, PIN6_CONFIG},
                   {PIN7, PIN7_CONFIG},
                   {PIN20, PIN20_CONFIG},
                   {PIN14, PIN14_CONFIG}
};
#endif /*_DIO_CONFIG_H*/
