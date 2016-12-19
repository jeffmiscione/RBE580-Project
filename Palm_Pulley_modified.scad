thumb_length = 65; middle_length = 80; palm_width = 85;

//length
module palm_pulley(thumb_length,middle_length,palm_width)
{    
    res = 30;
    difference(){
        union(){
            //palm part
            cube([palm_width*10/85,palm_width*25/85,palm_width/85]); 
            translate([0,palm_width*50/85,0])cube([palm_width*10/85,palm_width*35/85,palm_width/85]);
            translate([palm_width*75/85,palm_width*50/85,0]) cube([palm_width*10/85,palm_width*35/85,palm_width/85]);
            translate([palm_width*50/85,0,0]) cube([palm_width*10/85,palm_width*25/85,palm_width/85]);   
            translate([0,0,palm_width/85])cube([palm_width,palm_width,palm_width*2/85]);
        }
    
        union(){
            //palm cutout (thumb section)
            translate([palm_width*60/85,0,0])
            cube([palm_width*25/85,palm_width*25/85,palm_width*5/85],false);
            translate([palm_width,palm_width*50/85,0])
            rotate([0,0,-135])
            cube([(palm_width*25/85)/sin(45),palm_width*25/85,palm_width*5/85],false);
            //holes   
            //screw holes
            for(i=[0:1:1]){
                translate([palm_width*(5/85+50/85*i),palm_width*5/85,0])
                cylinder(10,r=3.46/2,false,$fn=50);
                translate([palm_width*(5/85+50/85*i),palm_width*20/85,0])
                cylinder(10,r=3.46/2,false,$fn=50);
            }
            for(i=[0:1:1]){
                translate([palm_width*(5/85+75/85*i),palm_width*55/85,0])
                cylinder(10,r=3.46/2,false,$fn=50);
                translate([palm_width*(5/85+75/85*i),palm_width*75/85,0])
                cylinder(10,r=3.46/2,false,$fn=50);
            }

            //internal screws
            translate([palm_width*64.31/85,palm_width*37/85,0]) cylinder(palm_width*4/85,r=2.38/2,true,$fn=res);
            for(i=[0:1:1]){
            translate([palm_width*(22.69+20*i)/85,palm_width*(37-i)/85,0]) cylinder(palm_width*5/85,r=2.38/2,true,$fn=res);
             
            translate([palm_width*(53.5-20*i)/85,palm_width*39/85,0]) cylinder(palm_width*5/85,r=2.38/2,true,$fn=res);

                
            translate([palm_width*(11.69+44*i)/85,palm_width*73/85,0]) cylinder(palm_width*5/85,r=2.38/2,true,$fn=res);
            translate([palm_width*(31.31+44*i)/85,palm_width*73/85,0]) cylinder(palm_width*5/85,r=2.38/2,true,$fn=res);
            }    
            //slant    
            translate([0,palm_width*77/85,palm_width*3/85]) rotate([360-10,0,0]) cube([palm_width,palm_width*50/85,palm_width*5/85]);
            //slots
            for(i=[0:1:1]){
                translate([palm_width*(44*i)/85,0,0])
                union(){
                    translate([palm_width*21.5/85,palm_width*65/85,palm_width/85]) cylinder(palm_width*2/85,r=1.64,true,$fn=res);
                    translate([palm_width*21.5/85,palm_width*45/85,palm_width/85]) cylinder(palm_width*2/85,r=1.64,true,$fn=res); 
                    translate([palm_width*19.86/85,palm_width*45/85,palm_width/85]) cube([palm_width*(1.64*2)/85,palm_width*20/85,palm_width*2/85]);
                    }
                }
                translate([palm_width*22/85,palm_width*-35/85,0])
                union(){
                    translate([palm_width*21.5/85,palm_width*65/85,palm_width/85]) cylinder(palm_width*2/85,r=1.64,true,$fn=res);
                    translate([palm_width*21.5/85,palm_width*45/85,palm_width/85]) cylinder(palm_width*2/85,r=1.64,true,$fn=res); 
                    translate([palm_width*19.86/85,palm_width*45/85,palm_width/85]) cube([palm_width*1.64*2/85,palm_width*20/85,palm_width*2/85]);
                }
            
        }
    }
    
    

}

palm_pulley(thumb_length,middle_length,palm_width);